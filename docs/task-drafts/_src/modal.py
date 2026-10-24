import csv, os
from lib import *
import alt_orders
T = "Modal verbs"
old = list(csv.reader(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "modal_base.csv"), encoding="utf-8-sig", newline="")))[1:]
drop = ("Nobody forces you, but you feel it is very important", "Your job needs a uniform. Which sentence shows a duty from outside?")
for r in old:
    if any(r[3].startswith(d) for d in drop): continue
    row = r[:8] + [""]
    if row[2] == "order":   # other correct orders (alt_orders.py)
        have = [x.strip() for x in row[5].replace("also accepted:", "").split("|") if x.strip()]
        more = [a for a in alt_orders.alternatives(row[4]) if a not in have]
        if more: row[5] = "also accepted: " + " | ".join(have + more)
    rows.append(row)
# ---- new, in the style of the course books (must / have to are both "necessary"; the contrast is mustn't / don't have to and the past)
mc(T,"A2.1",2,"Choose the correct word: ___ I use your phone, please?","Can",["Do","Am","Are"],"We ask for permission with *Can I ...?*","Atļauju lūdz ar *Can I ...?*")
mc(T,"A2.1",2,"Which sentence gives advice?","You should drink more water.",["You can drink water here.","You are drinking water.","You drank water."],"*Should* gives advice.","*Should* dod padomu.")
mc(T,"A2.2",2,"Choose the correct form: Children under five ___ pay for the bus. It is free.","don't have to",["mustn't","doesn't have to","haven't to"],"*Don't have to* = not necessary. *Children* is plural, so *don't*.","*Don't have to* = nav nepieciešams. *Children* ir daudzskaitlī, tāpēc *don't*.")
mc(T,"A2.2",2,"Which sentence means the same as 'It isn't necessary to book a table'?","You don't have to book a table.",["You mustn't book a table.","You can't book a table.","You must book a table."],"*Don't have to* means it is not necessary.","*Don't have to* nozīmē, ka tas nav nepieciešams.")
mc(T,"A2.2",2,"Which sentence means the same as 'You have to show your ticket'?","You must show your ticket.",["You mustn't show your ticket.","You don't have to show your ticket.","You can show your ticket."],"*Must* and *have to* both say it is necessary.","*Must* un *have to* abi saka, ka tas ir nepieciešams.")
mc(T,"A2.2",3,"A sign says: 'Photos are not allowed.' Which sentence is correct?","You can't take photos here.",["You don't have to take photos here.","You must take photos here.","You can take photos here."],"*Can't* + base verb says something is not allowed.","*Can't* + pamatforma nozīmē, ka tas nav atļauts.")
tx(T,"A2.2",3,"Make it negative: Tom has to work on Sundays.",["Tom doesn't have to work on Sundays.","Tom does not have to work on Sundays."],"Negative of *has to*: *doesn't have to* + base verb.","*Has to* noliegums: *doesn't have to* + pamatforma.")
gp(T,"A2.2",3,"Complete with have to or don't have to: It is Saturday, so I ___ get up early.","don't have to","On Saturday it is not necessary: *don't have to*.","Sestdienā nav nepieciešams: *don't have to*.")
od(T,"A2.2",3,"Put the words in order. Say it is not necessary.","you don't have to pay for parking here","Subject + *don't have to* + base verb.","Priekšmets + *don't have to* + pamatforma.")
mt(T,"A2.2",2,"Match each sign with its meaning.",[("No entry","You can't go in."),("Pay here","You have to pay."),("Free entry","You don't have to pay."),("Quiet, please","You should speak quietly.")],"*Can't* = not allowed, *have to* = necessary, *don't have to* = not necessary, *should* = advice.","*Can't* = nav atļauts, *have to* = nepieciešams, *don't have to* = nav nepieciešams, *should* = padoms.")
mc(T,"B1.1",3,"Choose the correct form: The test was cancelled, so we ___ study last night.","didn't have to",["couldn't","mustn't","hadn't to"],"*Didn't have to* = it was not necessary (past).","*Didn't have to* = nebija nepieciešams (pagātnē).")
mc(T,"B1.1",3,"Which sentence means it was not allowed?","We couldn't use our phones in the exam.",["We didn't have to use our phones in the exam.","We had to use our phones in the exam.","We could use our phones in the exam."],"*Couldn't* = not allowed in the past. *Didn't have to* = not necessary.","*Couldn't* = nebija atļauts pagātnē. *Didn't have to* = nebija nepieciešams.")
gp(T,"B1.1",3,"Complete with will have to: If the bus is late, we ___ take a taxi.","will have to | 'll have to","*Must* has no future form, so we use *will have to*.","*Must* nav nākotnes formas, tāpēc lieto *will have to*.")
mc(T,"B1.1",3,"You want to give polite advice, not an order. Choose the best option: You ___ see a doctor about that cough.","should",["must","have to","mustn't"],"*Should* is advice: a good idea. *Must* and *have to* sound like an order.","*Should* ir padoms: laba ideja. *Must* un *have to* izklausās pēc pavēles.")
mc(T,"B1.1",3,"Choose the correct option: He has worked all day without a break. He ___ be very tired.","must",["can't","mustn't","doesn't have to"],"*Must* can also show we are sure: *He must be tired.*","*Must* var arī izteikt pārliecību: *He must be tired.*")
mc(T,"B1.1",3,"Choose the correct option: Anna is on holiday in Spain, so that ___ be her in the photo.","can't",["must","has to","doesn't have to"],"*Can't* shows we are sure something is not true.","*Can't* parāda, ka esam pārliecināti, ka tas nav patiesi.")
tx(T,"B1.1",3,"Rewrite in the past: We don't have to wait.","We didn't have to wait.","Past of *don't have to* is *didn't have to*.","*Don't have to* pagātne ir *didn't have to*.")
tx(T,"B1.1",5,"Rewrite with must or have to: It is necessary for you to wear a helmet here.",["You must wear a helmet here.","You have to wear a helmet here."],"*Must* and *have to* both say it is necessary.","*Must* un *have to* abi saka, ka tas ir nepieciešams.")
tx(T,"B1.1",5,"Rewrite with mustn't: It is not allowed to use phones in the cinema.",["You mustn't use phones in the cinema.","You mustn't use your phone in the cinema.","You mustn't use your phones in the cinema.","We mustn't use phones in the cinema."],"*Mustn't* + base verb says it is not allowed.","*Mustn't* + pamatforma nozīmē, ka tas nav atļauts.")
mc(T,"B1.1",4,"Which sentence is a weak prohibition (it is better not to)?","You shouldn't talk loudly here.",["You mustn't talk loudly here.","You can't talk loudly here.","You don't have to talk loudly here."],"*Shouldn't* is a gentle 'better not'. *Mustn't* and *can't* are strong.","*Shouldn't* ir maigs 'labāk ne'. *Mustn't* un *can't* ir stingri.")
save("modal-verbs-1.csv")
