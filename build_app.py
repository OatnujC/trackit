import json
src=open("gen.py").read()
pre=src.split("for g in groups.values()")[0]
ns={}
exec(pre,ns)
groups=ns["groups"];T=ns["T"]
for g in groups.values():
    for e in g: e["img"]=T[e["vid"]]
data=json.dumps(groups,ensure_ascii=False)
shots_meta=json.load(open("shots.json"))
for s in shots_meta:
    s["img"]=T[s["vid"]]
shots=json.dumps(shots_meta,ensure_ascii=False)
html=open("app_template.html").read()
html=html.replace("__DATA__",data).replace("__SHOTS__",shots)
open("jt-workout-app.html","w").write(html)
print(len(html))
