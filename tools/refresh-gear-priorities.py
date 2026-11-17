"""Public aggregates -> unsigned review candidate. No character input or signing key."""
import argparse,json,hashlib,math
from pathlib import Path
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from urllib.parse import urlencode
p=argparse.ArgumentParser();p.add_argument('--reference',type=Path,required=True);p.add_argument('--tokens',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
db=json.loads(a.reference.read_text(encoding='utf-8'));tokens=json.loads(a.tokens.read_text(encoding='utf-8'));a.output.mkdir(parents=True,exist_ok=True)
jobs=dict(Gladiator='검성',Templar='수호성',Assassin='살성',Ranger='궁성',Sorcerer='마도성',Spiritmaster='정령성',Cleric='치유성',Chanter='호법성')
usage={};samples={}
for cls,job in jobs.items():
 url='https://cielui.com/api/item-stats?'+urlencode(dict(mode='pve',job=job))
 with urlopen(Request(url,headers={'User-Agent':'EZlay-Gear-Reference-Review/1.0'}),timeout=30) as response:raw=response.read(524289)
 if len(raw)>524288:raise ValueError('Aggregate exceeds size limit')
 data=json.loads(raw)
 if data.get('ready')!=True or data.get('job')!=job or data.get('mode')!='pve':raise ValueError('Wrong aggregate scope')
 slots={s['slot']:s for s in data['slots'] if isinstance(s.get('sample'),int) and s['sample']>0}
 if not slots:raise ValueError('No sample for '+cls)
 usage[cls]=slots;samples[cls]={s:v['sample'] for s,v in slots.items()}
changed=False;pools={}
for rule in db['Rules']:
 slot=usage[rule['Class']].get(rule['Slot'])
 if slot is None:raise ValueError('Previously supported slot lost its aggregate')
 weights={str(v['sid']):v['count']/slot['sample'] for v in slot.get('engrave',[])+slot.get('skills',[])}
 if any(not math.isfinite(w) or w<0 or w>1 for w in weights.values()):raise ValueError('Invalid usage share')
 old=db['Pools'][rule['PoolId']] if rule.get('PoolId') else rule['Options'];options=[]
 for option in old:
  key=str(option['Id']) if option['Kind']=='skill' else tokens[str(option['Id'])]
  fresh={**option,'Weight':round(weights.get(key,0),5)};options.append(fresh);changed|=fresh!=option
 if not any(o['Weight'] for o in options):raise ValueError('Reference loses all priorities')
 identity=hashlib.sha256(json.dumps(options,separators=(',',':')).encode()).hexdigest()[:20]
 if identity in pools and pools[identity]!=options:raise ValueError('Pool collision')
 pools[identity]=options;rule.update(Options=[],PoolId=identity)
now=datetime.now(timezone.utc).isoformat()
(a.output/'source-check.json').write_text(json.dumps(dict(CheckedAt=now,Changed=changed,CurrentRevision=db['Revision'],Published=False,Samples=samples),indent=2)+'\n',encoding='utf-8')
if changed:
 db.update(Schema=2,Pools=pools,Revision=db['Revision']+1,PublishedAt=now)
 for source in db['Sources']:
  if source['Id']=='pve-priorities':source['ObservedAt']=now
 (a.output/'candidate-reference.json').write_text(json.dumps(db,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
(a.output/'README.txt').write_text('Unsigned review candidate only. Global cap dates retained. Review and sign before publishing. No character records or signing key are used.\n',encoding='utf-8')
print('Priorities changed:',changed,'; published: false')
