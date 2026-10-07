"""Validate catalog before publishing; uses Python standard library only."""
import json, re, math
from pathlib import Path
root=Path(__file__).resolve().parents[1]/'public'
data=json.loads((root/'data/products.json').read_text())
assert data['schemaVersion']==1, 'Unsupported schema version'
seen=set()
for p in data['products']:
    assert re.fullmatch(r'[A-Za-z0-9_-]+',p['id']), 'Invalid product ID'
    assert p['id'] not in seen, f'Duplicate ID: {p["id"]}'
    seen.add(p['id'])
    for key in ('name','category','description'):
        assert isinstance(p[key],str) and p[key].strip(), f'{p["id"]}: missing {key}'
    assert p['category']!='全部', 'Reserved category'
    assert type(p['price']) in (int,float) and math.isfinite(p['price']) and p['price']>=0 and abs(p['price']*100-round(p['price']*100))<1e-6, 'Invalid price'
    assert p['currency']=='CNY', 'Only CNY is supported'
    assert p['status'] in ('上架','下架'), 'Invalid status'
    assert type(p['sort']) is int and p['sort']>=0, 'Invalid sort'
    assert isinstance(p.get('specs',{}),dict) and all(isinstance(v,str) for v in p.get('specs',{}).values()), 'Invalid specs'
    assert isinstance(p['images'],list) and p['images'], 'Images required'
    for path in p['images']:
        target=(root/path).resolve()
        assert target.is_relative_to(root.resolve()), 'Image path escapes public'
        assert target.is_file(), f'Missing image: {path}'
config=json.loads((root/'data/site.json').read_text())['contact']
assert type(config['demo']) is bool
assert all(isinstance(config[k],str) for k in ('wechat','email','note'))
assert config['demo'] or config['wechat'].strip() or config['email'].strip(), 'Contact method required'
print(f'PASS: {len(seen)} products, all image paths and contact settings valid.')
