import json
T=json.load(open('thumbs.json'))
def ex(name,sets,cue,vid,vt,ch,why=None,url=None):
    d=dict(name=name,sets=sets,cue=cue,vid=vid,vt=vt,ch=ch)
    if url: d["url"]=url
    return d
groups = {
"warmup":[
 ex("Isometric calf hold","2 × 45s","On the balls of your feet, heels slightly raised; hold still, breathe.","isVPZTr5iXk","Achilles Tendinopathy – Isometric Holds","NUH Singapore"),
 ex("Ankle mobility","2–3 min","Knee-to-wall rocks, then ankle circles; heel stays down.","IikP_teeLkI","Top 3 Ankle Mobility Exercises","Squat University"),
 ex("Dynamic leg swings","10 each way / leg","Front-back then side-to-side; tall torso, swing from the hip.","naW8u72lOzI","Leg Swings – Active Warm-Up","Runner's World"),
],
"plyo":[
 ex("Pogo hops","3 × 20","Stiff ankles, quick ground contact, bounce off the balls of the feet.","j0nl5dWuqN4","Pogo Jumps Tutorial – Proper Form","Runna"),
 ex("Scissor jumps in place","3 × 8","Switch legs in the air, land on the left foot, weight going forward.","nXudpuO6pMs","How To Do A Scissor Kick","Badminton Insight"),
 ex("Single-leg forward hop and stick","3 × 5 / leg","Land soft and quiet, knee over toes, hold 2s.","3_QHB0B9JyU","Single leg hop and stick","GameTime Sports & Training"),
 ex("Lateral bounds","3 × 6 / side","Push off the outside leg, stick the landing before the next bound.","Hc9_FQgIeeg","Lateral Bound","Nick Brattain"),
 ex("Reactive split-step hops","3 × 20s","Hop on the cue, land on the balls of your feet, push off the called way.","gy4YZS5tGxE","Badminton Footwork – The Split Step","Badminton Insight"),
],
"strength":[
 ex("Bulgarian split squat","3 × 8 / leg","Chest up, front knee over ankle.","hPlKPjohFS0","The Perfect Bulgarian Split Squat","Squat University"),
 ex("Single-leg RDL","3 × 8 / leg","Hip hinge with a flat back; hips stay square.","Zfr6wizR8rs","The Best Single-Leg RDL Tutorial","Squat University"),
 ex("Reverse lunge to knee drive","3 × 8 / leg","Step back, drive the knee up and through: your push back from the net.","pa3fq5cLeAA","Reverse Lunge to Knee Drive","E3 Rehab"),
 ex("Hip thrust","3 × 10","Chin tucked, ribs down, squeeze the glutes at the top.","xDmFkJxPzeM","Perfect Hip Thrust Technique","Jeff Nippard"),
 ex("Heavy single-leg calf raise off step","3 × 10–12 / leg","Dumbbell in hand, full range, 3s lowering below the step.","gUEffJQ2IdU","Deficit Single Leg Calf Raises","The Barefoot Sprinter"),
 ex("Bent-knee (soleus) calf raise","3 × 15","Knees bent, weight on the knees, slow up and down.","BxfKOyI8sUg","How to Do a Seated Calf Raise","Hinge Health"),
 ex("Face pulls","3 × 15","Pull to the face, elbows high, rotate the hands back.","eTCBSFlCJ_s","How to do a Face Pull","NASM"),
 ex("Band pull-aparts (alternative)","3 × 15","Straight arms, squeeze the shoulder blades, slow return.","stwYTTPXubo","How To Do Banded Pull-Aparts","Tangelo Chiropractic + Rehab"),
],
"core":[
 ex("Pallof press","3 × 10 / side","Press out and resist the twist; hips and shoulders stay square.","5_8d8vHgZvU","Pallof Press + Variations","Girls Gone Strong"),
 ex("Dead bug","3 × 8 / side","Lower back stays pressed down; opposite arm and leg move slowly.","GbSC02oU3To","How to Do a Dead Bug","Hinge Health"),
 ex("Side plank with reach","3 × 20s / side","Hips high, thread the top arm under and back up.","7lfNb_zydvQ","Side Plank with Reach Through","Theory of Motion"),
],
"cond":[
 ex("Bike or rower intervals","8 × 30s hard / 30s easy","Hard means you could not hold the pace for a minute. Rower: legs, body, arms.","4zWu1yuJ0_g","Correct Rowing Machine Technique","Concept2"),
],
"rehab":[
 ex("Isometric calf hold","4–5 × 30–45s","Balls of feet, heels slightly raised, hold still.","MYehmaMlKSs","Achilles Tendinopathy Stage 1: Isometric Calf Raises","Fix Physio"),
 ex("Straight-knee eccentric calf raise off step","3 × 15","Up on two feet, lower slowly on one below the step. Progress to single leg, then weighted.","fHHbn_Odk4E","Alfredson Achilles Rehab Protocol","Physiotutors"),
 ex("Bent-knee calf raise","3 × 15","Knees bent to load the soleus, slow lowering.","uJ7QH7pExh0","Seated Soleus Calf Raises","The Physio Fix"),
 ex("Tibialis raises against wall","2 × 15","Back on the wall, heels forward, lift the toes high.","VzIcGAgBiaM","Tibialis Wall Raises","The Barefoot Sprinter"),
 ex("Single-leg balance","3 × 30s / leg","Soft knee, steady foot; progress to a cushion.","7SF7AYh2_Yw","Single Leg Balance Exercise","Coury & Buehler PT"),
],
"recovery":[
 ex("Easy swim","20–30 min","Conversational pace, smooth breathing. Finish 2–4 hours before bed. No pool? Do the easy bike instead.","REC_swim","Recovery cardio","Coach note",url="NONE"),
 ex("Easy bike (alternative)","20–30 min","Light resistance, steady cadence, you can still talk. Save hard intervals for earlier in the day.","REC_bike","Recovery cardio","Coach note",url="NONE"),
 ex("Sauna, then cool shower","10–15 min + 2 min","Sit in the sauna, then a cool shower. Drink 500 ml or more of water after: you sweat heavily.","REC_sauna","Recovery & sleep","Coach note",url="NONE"),
],
"home":[
 ex("Wall lunge check","3 × 8 / leg","Front knee stops short of the wall, chest tall.","oT1VDVUjGxY","The 6 Keys for a Perfect Lunge in Badminton","Tobias Wadenka"),
 ex("Split-step multi-direction lunges","3 × 6 / direction","Split step, lunge forward, diagonal or side with chest up and knee over toes, then explode back to base in one push.","IG_Dej4VY","Why this exercise is so good for badminton","madsdrostchristophersen · Instagram",url="https://www.instagram.com/p/Dej4VY-ilJI/"),
 ex("Shadow lunge and push back","3 × 30s","Lunge to the net, then 2 quick chasse steps back while facing forward.","ive-Vf8BmH4","Frontcourt Footwork: Basic to Advanced","Tobias Wadenka"),
 ex("Racket-up shadow footwork, 6 corners","4 × 30s","Racket head above your hand, split step every time you leave base.","a7ajExQKOvY","6 Corners Footwork for Badminton","Jacobs Badminton"),
 ex("Backhand shadow swings (towel or band)","3 × 15","Turn early, elbow up, snap through.","HWdY4wyERSA","Backhand Clear, Basic Tutorial","Shuttle Life"),
 ex("Wrist and forearm: rice bucket or light dumbbell","2 × 30s","Rotations both ways; controlled, not fast.","vvximWI1-JM","Hand & Wrist Strength: Rice or Sand Bucket","Catalyst Athletics"),
],
"drill_net":[
 ex("Wall taps (short finger snap)","3 × 30s","Solo. Racket up, elbow in front, pinch then squeeze. Stop the racket dead after contact. Cue: tap, not swing.","DR_walltap","Net kill wall taps","Coach note",url="NONE"),
 ex("Partner net-kill feed","2 × 10 each","Partner. Both stand near the net. Feed tight or slightly high; kill anything above the tape with a finger snap. Swap feeder every 10.","DR_netkill","Partner net-kill feed","Coach note",url="NONE"),
 ex("Kill-or-net decision","3 × 2 min","Partner. Rally at the net: if the shuttle is above the tape, kill; if tight to the tape, soft net. Call it out loud before you hit.","DR_killnet","Kill-or-net decision","Coach note",url="NONE"),
 ex("Elbow-on-wall check / choke up","2 × 10","Solo. Stand with elbow lightly on a wall, choke up on the grip, snap with fingers only. Then take the same feel onto court.","DR_elbow","Elbow-on-wall grip check","Coach note",url="NONE"),
 ex("Say \"tap\" out loud","During net drills","Solo or partner. Say \"tap\" on every kill so the swing stays short. If you hear yourself going quiet, the arm is taking over.","DR_tap","Net kill verbal cue","Coach note",url="NONE"),
],
"drill_receive":[
 ex("Racket-up receive vs short and flick","2 × 10 each","Partner. Both receive. Hold racket at head height, left foot forward, loose grip. Partner mixes short serves and flicks; push short ones, turn and clear flicks.","DR_recv","Serve receive practice","Coach note",url="NONE"),
 ex("Flick-recovery turn","3 × 8","Partner or solo shadow. From receive stance, on a flick cue push off the front foot, turn sideways and get the racket above the head — never drop it to the waist first.","DR_flick","Flick serve recovery","Coach note",url="NONE"),
],
"drill_early":[
 ex("Split-step reaction","3 × 30s","Partner. Split step as they \"hit\", then they point to a corner. Move, shadow the shot, recover. Swap every set so both train.","DR_split","Split-step reaction","Coach note",url="NONE"),
 ex("Fast mid-court drives","3 × 45s","Partner. Flat drives at mid-court. Cue: hit it before it crosses your body. Both push each other back.","DR_drives","Fast mid-court drives","Coach note",url="NONE"),
 ex("Net kill-or-push","3 × 2 min","Partner. Both near the net. Play tight net shots; anything above the tape, kill or push straight away. Take it high and early.","DR_killpush","Net kill-or-push","Coach note",url="NONE"),
 ex("Half-court rally (above net only)","2 × 5 min","Partner. Point only counts if you hit above net height. Forces early contact.","DR_halfct","Half-court early-contact rally","Coach note",url="NONE"),
 ex("Multi-shuttle feed","2 × 20 shuttles each","Partner. Feeder throws or hits quickly to random spots. Take each before it drops below the tape, then swap.","DR_multi","Multi-shuttle early take","Coach note",url="NONE"),
],
"drill_rear":[
 ex("Net-to-rear shadow","3 × 8 / corner","Solo. Lunge at the net, push back to base, split step, then go to a rear corner (forehand or round-the-head) and shadow a clear. Cue: turn first, then move.","DR_netrear","Net-to-rear shadow footwork","Coach note",url="NONE"),
 ex("Turn-and-go reaction","10 / side","Partner. Start at the net racket up; on their call, turn, one crossover, jump to the rear corner. Trains the first step. Swap every 10.","DR_turngo","Turn-and-go reaction","Coach note",url="NONE"),
 ex("Lift-chase two-shot","2 × 10 each","Partner. They play a net shot, you net it, they lift deep. Chase and hit an attacking clear or smash. Reply is a net shot so both keep moving.","DR_liftchase","Lift-chase two-shot drill","Coach note",url="NONE"),
 ex("Intercept high","2 × 5 min","Partner. Half-court rally with lower, faster lifts. Hit every shot with a jump at the highest point — never let it drop behind your head.","DR_intercept","Intercept high","Coach note",url="NONE"),
 ex("Malaysian step (L-R-L) shadow","3 × 6 / side","Solo, half speed first. Left-right-left chassé into a one-leg jump for fast flat lifts round the head. Achilles note: build up gradually; stiff next morning → two-footed only.","DR_malay","Malaysian step footwork","Coach note",url="NONE"),
 ex("Cross step + scissor kick shadow","3 × 6 / side","Solo, half speed first. Cross behind, plant, full rotational scissor-kick jump. Use when the clear is high and you have time.","DR_cross","Cross step scissor kick","Coach note",url="NONE"),
 ex("Recovery race","During rear drills","Solo or partner. After every shot from the back, sprint back to base before the shuttle lands on their side.","DR_recrace","Recovery race","Coach note",url="NONE"),
],
"drill_depth":[
 ex("Clears to the back tramlines","2 × 20","Partner. Rally clears aiming for the gap between the back two lines. Short of the doubles service line = miss.","DR_tramline","Clear depth tramlines","Coach note",url="NONE"),
 ex("Hip-first slow shadow swings","3 × 10","Solo. Turn sideways, belt buckle to the net first, wait a beat, then let the arm follow. Speed up once the order feels automatic.","DR_hipshadow","Hip-first shadow swings","Coach note",url="NONE"),
 ex("Med-ball rotational throws","3 × 8 / side","Solo or partner. Hips turn first, then the ball flies. Closest gym match to a smash.","DR_medball","Med-ball rotational throws","Coach note",url="NONE"),
],
"drill_lunge":[
 ex("Split-step multi-direction lunges","3 × 6 / direction","Split step, lunge forward, diagonal or side with chest up and knee over toes, then explode back to base in one push.","IG_Dej4VY","Why this exercise is so good for badminton","madsdrostchristophersen · Instagram",url="https://www.instagram.com/p/Dej4VY-ilJI/"),
 ex("V-front lunges (heel-to-toe plant)","3 × 6 / side","Solo. From base, lunge on a V path to the front corners. Plant heel-to-toe, knee over toes, chest up.","DR_vfront","V-front lunges","Coach note",url="NONE"),
 ex("Push back through front heel","3 × 8 / leg","Solo. From a net lunge, drive through the front heel and push the hips back to base — don't lead with the shoulders.","DR_heelpush","Heel-drive recovery","Coach note",url="NONE"),
 ex("Scissor-kick landing practice","3 × 8","Switch legs in the air, land on the left foot with weight going forward — not a two-footed stick that falls back.","nXudpuO6pMs","How To Do A Scissor Kick","Badminton Insight"),
],
"drill_hips":[
 ex("Hip thrust","3 × 10","Chin tucked, ribs down, squeeze the glutes at the top. Teaches hips to drive.","xDmFkJxPzeM","Perfect Hip Thrust Technique","Jeff Nippard"),
 ex("Single-leg RDL","3 × 8 / leg","Hip hinge with a flat back; hips stay square. Cue: bum back, chest up.","Zfr6wizR8rs","The Best Single-Leg RDL Tutorial","Squat University"),
 ex("Med-ball rotational throws","3 × 8 / side","Hips first, arm follows. Same as in Clear depth — do them here when the focus is power.","DR_medball","Med-ball rotational throws","Coach note",url="NONE"),
 ex("Hip-first shadow swings","3 × 10","Belt buckle to the net, then the arm. Slow then fast.","DR_hipshadow","Hip-first shadow swings","Coach note",url="NONE"),
],
"drill_fit":[
 ex("Easy base swim / bike / jog","30–40 min","Conversational pace — you could still hold a chat. Builds recovery between rallies. Your Wed/Sun swims count.","DR_easyjog","Easy base cardio","Coach note",url="NONE"),
 ex("Shadow footwork intervals","10 × 20s / 20s rest","All-out shadow to the corners for 20s, rest 20s. Progress: cut rest to 15s or add rounds.","DR_intervals","Badminton shadow intervals","Coach note",url="NONE"),
 ex("Rest and drink between drill sets","Every set","30–60s between sets, slow nose breathing, drink on every break. Being gassed is often dehydration plus starting too hard.","DR_restdrink","Rest & hydrate between sets","Coach note",url="NONE"),
 ex("Easy swim (recovery option)","20–30 min","Conversational pace, smooth breathing. Finish 2–4 hours before bed.","REC_swim","Recovery cardio","Coach note",url="NONE"),
],
}
for g in groups.values():
    for e in g: e['img']=T[e['vid']]
data=json.dumps(groups,ensure_ascii=False,indent=0)
tsx = r'''import { Page, Section, Text, Table, Grid, Image, Properties, LinkCards, Callout, Rows, TableOfContents } from "grok/canvas";

type Ex = { name: string; sets: string; cue: string; vid: string; vt: string; ch: string; img: string };
const G: Record<string, Ex[]> = __DATA__;

function cards(list: Ex[]) {
  return (
    <Grid columns={3}>
      {list.map((e: Ex) => (
        <Section key={e.vid + e.name} heading={e.name}>
          <Image src={e.img} alt={"Video thumbnail: " + e.vt + " (" + e.ch + ")"} fit="cover" height={140} />
          <Properties items={[{ label: "Sets × reps", value: e.sets }, { label: "Cue", value: e.cue }]} />
          <LinkCards links={[{ title: e.vt, site: e.ch + " · YouTube", href: "https://www.youtube.com/watch?v=" + e.vid }]} />
        </Section>
      ))}
    </Grid>
  );
}

export default function App() {
  return (
    <Page
      width="wide"
      title="JT's Badminton Gym & Home Plan"
      summary="A weekly gym, Achilles rehab and home programme built around the faults in your match videos, with a demo video for every exercise."
    >
      <TableOfContents items={[
        { label: "Why this plan", id: "why" },
        { label: "Weekly schedule", id: "week" },
        { label: "Gym 1: Warm-up", id: "gym1" },
        { label: "Gym 2: Plyometrics", id: "gym2" },
        { label: "Gym 3: Strength", id: "gym3" },
        { label: "Gym 4: Core", id: "gym4" },
        { label: "Gym 5: Conditioning", id: "gym5" },
        { label: "Calf and Achilles rehab day", id: "rehab" },
        { label: "Home routine (15–20 min)", id: "home" },
        { label: "Coaching cues", id: "cues" },
      ]} />

      <Section heading="Why this plan" id="why">
        <Text>It targets what your match videos showed: two-footed smash landings that fall backwards (the scissor kick is not showing in games), net lunges where your torso folds and your knee goes past your toes with a slow walking recovery, your racket dropping below your waist, a late and low deep backhand, a weak split step, and fading after about 7 to 8 minutes. Your Achilles tendinopathy is mostly healed and you jump pain-free, so the full plyometrics stay in, with calf and Achilles strengthening built around them.</Text>
      </Section>

      <Section heading="Weekly schedule" id="week">
        <Table
          columns={["Day", "Session"]}
          rows={[
            ["Monday", "Gym + calf rehab"],
            ["Tuesday", "Home routine + court"],
            ["Wednesday", "Calf rehab only"],
            ["Thursday", "Gym + calf rehab"],
            ["Friday", "Home routine + isometric holds"],
            ["Saturday", "Matches"],
            ["Sunday", "Rest"],
          ]}
        />
        <Text>No heavy legs or calf day the day before you play.</Text>
      </Section>

      <Section heading="Gym 1: Warm-up" id="gym1" caption="Gym session is about 65 min. Open a video card to watch the demo on YouTube.">
        {cards(G.warmup)}
      </Section>

      <Section heading="Gym 2: Plyometrics (do these fresh)" id="gym2">
        {cards(G.plyo)}
      </Section>

      <Section heading="Gym 3: Strength" id="gym3">
        {cards(G.strength)}
      </Section>

      <Section heading="Gym 4: Core" id="gym4">
        {cards(G.core)}
      </Section>

      <Section heading="Gym 5: Conditioning" id="gym5">
        {cards(G.cond)}
      </Section>

      <Section heading="Calf and Achilles rehab day (Wednesday, about 20 min)" id="rehab">
        <Callout lead="Achilles rule" tone="warning">Pain up to 3 out of 10 during the work is OK if it has settled by the next morning. If it is worse the next morning, drop to two-footed jumps for a session or two, then build back up.</Callout>
        {cards(G.rehab)}
      </Section>

      <Section heading="Home routine (15–20 min)" id="home">
        {cards(G.home)}
      </Section>

      <Section heading="Coaching cues" id="cues">
        <Rows rows={[
          { title: "Chest proud in the lunge", detail: "Hinge from the hip crease with a flat back; never fold at the waist. Knee over ankle, not past the toes." },
          { title: "Scissor, land, go", detail: "Switch legs in the air on every smash, land on the left foot and move forward to the net." },
          { title: "Racket up after every shot", detail: "Racket head back in front of your chest before your opponent hits." },
          { title: "Morning-after Achilles check", detail: "Stiff or sore the morning after jumping means two-footed jumps only for a session or two." },
        ]} />
      </Section>
    </Page>
  );
}
'''
open('page.tsx','w').write(tsx.replace('__DATA__',data))
print(len(tsx)+len(data))
