"""Episode body content for Founders batch-11 summaries."""

EPISODES: dict[str, dict] = {
    "fnd-415-how-elon-thinks": {
        "keywords": ["TSLA", "Private:SpaceX", "First Principles"],
        "conclusion": "Jorgenson's Book of Elon distills decades of interviews into first-principles thinking, delete/simplify engineering, and mission-first endurance. Battery packs priced at $600/kWh versus ~$80 in London Metal Exchange materials; Falcon 1 Flight 4 saved SpaceX before NASA's $1.6 billion cargo deal. TSLA and Private:SpaceX compound when founders question requirements, integrate vertically, and treat physics as the only honest judge.",
        "background": "Senra reads Eric Jorgenson's The Book of Elon — thousands of hours compiling Musk's own words. Musk frames legacy as accuracy plus doing right for future consciousness; success is useful work multiplied by people helped. He rejects starting companies for money — ask what should exist, then make it happen even if cash is lost.\n\nCore themes repeat across Zip2, PayPal, Tesla, and SpaceX: first-principles reasoning over analogy, idiot-index costing, five-step engineering (question requirements, delete, simplify, accelerate, automate — in that order), front-line leadership, and maniacal urgency. Musk cites Isadore Sharp's 'Excellence is the capacity for pain' and warns startup years are hell — adrenaline mode burns 20-somethings who skip smelling roses.",
        "important_facts": [
            "Musk applies first principles to batteries: industry assumed $600/kWh packs when cobalt, nickel, aluminum, and steel bought on the London Metal Exchange cost ~$80/kWh in materials — the gap is process waste, not physics.",
            "SpaceX vendor quoted a $120,000 actuator; in-house build cost ~$3,900 — the idiot index. Three Falcon 1 failures 2006–2008 left one September 2008 cash attempt; Flight 4 success won NASA's $1.6 billion cargo contract six months later.",
            "Tesla Model 3 Gigafactory delete rampage removed turntables and handoffs; Musk's five-step algorithm forbids automating before deleting — he once tore out robots after wrongly accelerating broken processes. Burn rate framed as $100,000/day — a half-hour delay at 2 billion/week revenue costs ~$100 million.",
        ],
        "mental_model": {
            "name": "First Principles Delete Loop",
            "components": "Reason from physics, not analogy. Assign every requirement an owner; delete unowned specs. Separate engineering from management so designers feel pain. Attack the constraint; pressure and necessity fuel creativity. Development prototypes may explode; crewed operations stay conservative.",
            "application": "TSLA margins improve when BOM lines disappear and factories own the stack — battery, pack, electronics, drivetrain vertically integrated to escape supplier tiers. Private:SpaceX's 2% materials insight mirrors Tesla casting bets. Investors track whether simplification culture survives scale without talent burnout.",
        },
        "key_insights": [
            {
                "view": "Analogy hides waste; physics exposes it.",
                "question": "How did Musk reframe battery economics?",
                "answer": "Analysts copied past $600/kWh assumptions. Musk priced raw materials on the London Metal Exchange (~$80/kWh) and asked why clever assembly couldn't close the gap — same first-principles move as rocket actuator costing from $120k to $3.9k.",
            },
            {
                "view": "Delete before automate — always.",
                "question": "What is Musk's five-step engineering algorithm?",
                "answer": "Question requirements, delete, simplify, optimize, accelerate, then automate — reversing the order is digging faster. SpaceX email demanded 'ultra hardcore simplification'; Model 3 production removed unnecessary turntables after mistakenly automating first.",
            },
            {
                "view": "Mission intensity has a human price.",
                "question": "Why aren't there more Musks?",
                "answer": "Musk warns years of torture, rage-in-the-skull drive, and burning candles at both ends with a flamethrower — adrenaline survival mode hurts 20-somethings who never stop to smell roses. Perseverance comes because Mars and consciousness expansion feel simply important.",
            },
        ],
        "top_investment_implications": [
            {
                "ticker": "TSLA",
                "direction": "Long",
                "confidence": "Medium",
                "thesis": "Delete-first ops and vertical integration explain iteration speed on batteries and manufacturing — watch delegation risk as Musk splits time across five entities.",
            },
            {
                "ticker": "Private:SpaceX",
                "direction": "Long",
                "confidence": "Medium",
                "thesis": "Same first-principles costing and integration that saved Flight 4 underpin launch cadence and Starlink optionality — physics as judge, not wishful thinking.",
            },
        ],
        "golden_quotes": [
            "Excellence is the capacity for pain — Musk cites Four Seasons founder Isadore Sharp on enduring startup hell.",
            "Battery materials ~$80/kWh on the exchange versus $600/kWh packs — first principles expose process markup, not impossibility.",
            "Delete, simplify, then automate — Musk tore robots out after accelerating processes that should not have existed.",
        ],
        "chronology": {
            "subject": "Elon Musk",
            "events": [
                {"date": "1990s", "event": "Zip2 and x.com era; fake server rack and PayPal merger."},
                {"date": "2002", "event": "SpaceX founded; Mars mission, rockets as financing vehicle."},
                {"date": "2006–2008", "event": "Three Falcon 1 failures; Flight 4 succeeds September 2008."},
                {"date": "2008", "event": "NASA $1.6 billion cargo contract six months after Flight 4."},
                {"date": "2004+", "event": "Tesla join; Gigafactory delete rampage and vertical integration."},
                {"date": "2020s", "event": "Jorgenson compiles Book of Elon from decades of primary sources."},
            ],
        },
    },
    "fnd-417-arnold-schwarzenegger": {
        "keywords": ["Private:Schwarzenegger", "Brand Building", "Mental Toughness"],
        "conclusion": "Arnold's 1977 Education of a Bodybuilder — written at 30 — maps bodybuilding discipline onto Hollywood and business: visualization, six workouts weekly, and pain-as-progress. Mr. Universe at 20 after military jail for AWOL; mail-order empire and concentration beat rivals. Same principles he later applied to movies, politics, and Raising Cane's-style fanatical operator Todd Graves.",
        "background": "Senra reads Arnold Schwarzenegger's Education of a Bodybuilder, written at 30 in 1977 — a rare early blueprint like young Elon sketching SpaceX decades ahead. At 15 Arnold chose bodybuilding over team sports because only individual recognition satisfied him. Reg Park's Hercules photo became fixed ideal; he trained six days weekly when peers managed two or three.\n\nFather called him sick in the head; Arnold replied he would be the best-built man in the world, then go to America and act. Military AWOL for Junior Mr. Europe led to seven days on a cold stone bench — trophy worth it. Losses became data: secret sauce was concentration on standard exercises with higher reps, not novelty.",
        "important_facts": [
            "At 15 Arnold rode 8 miles to the gym; after first leg day he fell off his bike — soreness proved progress. He escalated to six workouts weekly when most trained two or three; father baffled, Arnold answered: 'I will be the best-built man in the world.'",
            "AWOL during army basic training for Junior Mr. Europe — caught climbing the wall, seven days military jail on a cold stone bench with almost no food; won the trophy anyway and doubled training to four hours twice daily.",
            "After a third-place loss he photographed winners, analyzed weaknesses, and fixed them with concentration on basics — next contest he placed second, peers ecstatic; Arnold saw only the gap to first. Mail-order courses, seminars, and gym membership grew 70 to 200 members using contest publicity.",
        ],
        "mental_model": {
            "name": "Visualize Then Outwork",
            "components": "Fix a hero image (Reg Park), paste photos on walls, and train through pain because soreness signals growth. Eliminate distractions — even parents — when emotions threaten focus. Measure calves and arms monthly; self-talk until destiny feels inevitable. Apply sport discipline to every new arena.",
            "application": "Founders entering new fields should transplant proven routines rather than reinvent motivation. Arnold's three-part formula — self-confidence, positive attitude, honest vision — scaled from Austria's ~20 bodybuilders to global brand. Concentration beats exotic programs; visualization without measurement is fantasy.",
        },
        "key_insights": [
            {
                "view": "Pain is feedback, not punishment.",
                "question": "Why did Arnold keep training when he could barely comb his hair?",
                "answer": "First leg day left him too weak to ride home — muscles stiff, whole body buzzing. Mother asked why; Arnold learned soreness meant growth. He chose an unpopular sport precisely because total energy devotion was possible.",
            },
            {
                "view": "Losses require honest autopsy.",
                "question": "What changed after placing third?",
                "answer": "He photographed winners, identified who beat him, and dropped novelty exercises for concentrated basics with higher repetitions — secret was concentration on painful shortcomings, not new machines.",
            },
            {
                "view": "Discipline transfers across careers.",
                "question": "How did bodybuilding become a business blueprint?",
                "answer": "Arnold writes the stuff of bodybuilding applies everywhere — mail-order courses, posing trunks, seminars across 15 countries, and gym membership growth from 70 to 200 using contest showmanship. Same visualization that built calves built Hollywood.",
            },
        ],
        "top_investment_implications": [
            {
                "ticker": "Private:Schwarzenegger",
                "direction": "Watch",
                "confidence": "Low",
                "thesis": "Arnold's operator playbook — visualization, measurement, publicity loops — is the lens for personal-brand businesses even without a tradable equity; Raising Cane's Todd Graves mirrors the fanatical daily routine.",
            }
        ],
        "golden_quotes": [
            "I will be the best-built man in the world — teenage Arnold to a baffled father.",
            "The secret is concentration — minutes spent painfully focused on shortcomings, not exotic exercises.",
            "The stuff of bodybuilding applies everywhere — Arnold's bridge from sport to movies and business empire.",
        ],
        "chronology": {
            "subject": "Arnold Schwarzenegger",
            "events": [
                {"date": "Age 15", "event": "Chooses bodybuilding; Reg Park photo becomes fixed ideal."},
                {"date": "Teens", "event": "Six workouts weekly; 8-mile bike rides to gym."},
                {"date": "Age 18", "event": "Army service; AWOL for Junior Mr. Europe; seven days jail."},
                {"date": "Age 20", "event": "Wins Mr. Universe; doubles training to four hours twice daily."},
                {"date": "1977", "event": "Publishes Education of a Bodybuilder at age 30."},
                {"date": "1970s–80s", "event": "America, acting, mail-order empire, Mr. Olympia dominance."},
            ],
        },
    },
    "fnd-413-how-to-run-down-a-dream": {
        "keywords": ["Private:87Capital", "Career Design", "Analytics"],
        "conclusion": "Gurley's Running Down a Dream profiles Sam Hinkie — valedictorian to Bain to Rockets GM at 27 on an inflatable mattress, then 76ers rebuild and 87 Capital VC. Gurley buckets Bobby Knight, Dylan, and Danny Meyer as dream-chasers: deep interest, craft obsession, mentors, peers, and go-giver service. Pick passion over status; information is freely available.",
        "background": "Senra reads Bill Gurley's Running Down a Dream — expanded from a 2018 MBA talk profiling Sam Hinkie and legendary operators. Hinkie grew up in Marlow, Oklahoma (population under 5,000), valedictorian, Bain hire, then quit for sports analytics after Moneyball and Theo Epstein's 2002 Red Sox.\n\nHe emailed every NFL team offering unpaid work, road-showed five teams over spring break while classmates hit Aruba, and slept on an inflatable mattress in Houston at 27 as Rockets special assistant. Les Alexander and Daryl Morey shared bond-trader philosophy; Hinkie later joined 76ers at 35. Gurley extracts five strains: deep interest, win-by-preparing, hone craft, develop mentors, embrace peer network — plus go-giver generosity.",
        "important_facts": [
            "Hinkie interned at Ernst & Young on sports-team valuations, joined Bain as first Oklahoma hire, quit ~18 months in after mentors laughed at 'Sports GM' — then read Moneyball in days and chased analytics full time.",
            "Spring break road show: visited five NFL teams while classmates vacationed; Houston Texans internship lasted eight weeks, then stuck — flying Palo Alto to Houston repeatedly. At 27 he became Rockets special assistant, sleeping on an inflatable mattress working 6 a.m. to midnight.",
            "2020: launched 87 Capital VC — name from Robert Caro's Means of Ascent: Lyndon Johnson won a 1948 Senate race by 87 votes. Gurley profiles Knight (902 victories), Dylan ($10 and 1,200 miles to NYC), Meyer (quit law school, $12,000 negative net worth opening Union Square Cafe).",
        ],
        "mental_model": {
            "name": "Run Down the Dream",
            "components": "Pick a deep interest — not status careers that burn out. Prepare to win (Knight sat next to coaches at luncheons). Hone craft obsessively (Dylan studied every folk album nine months). Collect mentors (Burritos with Parag Marathe). Build peer network with zero-sum-free sharing. Give credit and gifts — go-giver service compounds.",
            "application": "Founders choosing markets should ask Gurley's filter: immense passion plus use-it-or-lose-it life. Hinkie's unpaid NFL pitches mirror Dylan's hitchhike — information is free; execution differentiates. Hire aptitude and attitude; skills train later (Kelly maxim echoed).",
        },
        "key_insights": [
            {
                "view": "Status careers fake; passion shows.",
                "question": "Why quit Bain for sports?",
                "answer": "When mentors asked 'if you could do anything,' Hinkie said Sports GM — they laughed. Moneyball plus Theo Epstein becoming youngest GM at 28 proved analytics disruption real. He quit lucrative consulting to chase a dream parents thought crazy.",
            },
            {
                "view": "Earn influence before earning title.",
                "question": "How did Hinkie enter the NFL?",
                "answer": "Emailed and mailed every franchise offering unpaid intern work on salary-cap analytics; spring break road show hit five teams in one week. Texans eight-week stint became multi-year foothold via relentless value-add without burdening staff.",
            },
            {
                "view": "Generosity is networking that scales.",
                "question": "What is Gurley's go-giver principle?",
                "answer": "Celebrate peers, share non-proprietary knowledge, send gifts and letters — Knight passed Pete Newell's clinics to Coach K. Trading smart beats hoarding; worry about failing to advance, not failing to share.",
            },
        ],
        "top_investment_implications": [
            {
                "ticker": "Private:87Capital",
                "direction": "Watch",
                "confidence": "Low",
                "thesis": "Hinkie's 87 Capital applies bond-trader risk framing to venture — underwriting dreamers who run down passions with analytics discipline; no public float but useful lens for sports-tech and decision-science founders.",
            }
        ],
        "golden_quotes": [
            "Life is a use-it-or-lose-it proposition — Gurley on immense passion over status careers.",
            "Two ears, one mouth — use in proportion — Hinkie's advice to students after the 76ers journey.",
            "87 votes — Means of Ascent margin that names Hinkie's venture firm.",
        ],
        "chronology": {
            "subject": "Sam Hinkie · Bill Gurley",
            "events": [
                {"date": "2000s", "event": "Bain Capital; Ernst & Young sports valuation exposure."},
                {"date": "2002", "event": "Moneyball published; Epstein named Red Sox GM at 28."},
                {"date": "Mid-2000s", "event": "NFL road show; Rockets inflatable-mattress years."},
                {"date": "2013", "event": "Named 76ers GM at 35."},
                {"date": "2018", "event": "Gurley MBA talk on running down a dream."},
                {"date": "2020", "event": "Launches 87 Capital venture firm."},
            ],
        },
    },
    "fnd-412-how-roger-federer-works": {
        "keywords": ["NKE", "Mental Performance", "Longevity"],
        "conclusion": "Clare's The Master plus Federer's Dartmouth address: 1,526 matches, ~80% wins, but only ~54% of points won — champions move on fast. Psychologist Christian Marcoli rebuilt emotional control; Bowerman's stress-recover-improve loop and 2018 Uniqlo $300M deal show brand outlasting Nike athlete era. NKE parallels athlete-equity craft; Federer's longevity is systematic recovery plus present-moment focus.",
        "background": "Senra reads Christopher Clare's The Master — a performance-focused Federer biography — alongside his Dartmouth commencement. Young Federer threw rackets; opponents said he would lead for two hours then fade. Peter Carter, Pierre Paganini, and Mirka Vavrinec formed a decade-long team emphasizing recovery equal to training.\n\nAt 19 Federer beat Sampras at Wimbledon 2001; by 21 he addressed racket-throwing as career-defining image risk. Marcoli collaboration from age ~22 built emotional bubble — flames converted to slow fuel. Post-retirement: 2013 Forbes estimated $71M income; 2018 Uniqlo $300M decade deal plus On shoe stake in Zurich.",
        "important_facts": [
            "Federer's Dartmouth math: 1,526 career matches, ~80% match wins, but only ~54% of points won — even the greatest lose nearly every second point; dwelling on errors wastes energy opponents also feel.",
            "Teenage Federer had heart rate ~30 beats above normal in pressure moments, leading to racket abuse; psychologist Christian Marcoli from age ~22 taught systematic emotion management — calm exterior, boiling interior converted to fuel.",
            "2013 Forbes listed Federer world's highest-paid athlete at ~$71M; 2018 Uniqlo 10-year apparel deal ~$300M with On Running shoe investment — personalized sponsor suite meetings, not rushed CEO handoffs.",
        ],
        "mental_model": {
            "name": "Point-by-Point Recovery",
            "components": "Effortlessness is myth — meticulous planning and self-doubt backstage. Bowerman: stress, recover, improve — skipping rest equals injury. Trust talent but engineer support (Carter, Paganini, Marcoli). Compete present-moment; fear projects future shots not yet taken. Longevity via minimum burnout practice and protected family time.",
            "application": "Operators mirroring Federer build seamless trust webs — Charlie Munger's deserved-trust idea applied to coaches and spouses. NKE and Uniqlo bets reward athletes who protect brand composure; founders should treat emotional regulation as trainable infrastructure, not personality.",
        },
        "key_insights": [
            {
                "view": "Winning matches ≠ winning points.",
                "question": "What is Federer's 54% lesson?",
                "answer": "Even world No. 1 wins barely half of points — champions teach themselves to move on after double faults. Negative energy is wasted; opponents suffer self-doubt too. Relentless adaptation beats perfectionism on last shot.",
            },
            {
                "view": "Recovery is half the program.",
                "question": "How did Paganini change Federer at 17?",
                "answer": "Bowerman via Paganini: stress-recover-improve — rest is mechanism for work, not laziness. Teen Federer learned intelligent restraint after willed overtraining; fresh head equals fresh body for a 70-year career horizon.",
            },
            {
                "view": "Brand composure is moat.",
                "question": "Why did Federer fix racket-throwing at 21?",
                "answer": "2001 Sampras win brought fame; he realized TV tantrums risked career-defining image. Marcoli built bubble — outside calm, inside fire channeled to fuel. Olympic gold at 19 with 43rd ATP title showed discipline business rewards.",
            },
        ],
        "top_investment_implications": [
            {
                "ticker": "NKE",
                "direction": "Watch",
                "confidence": "Low",
                "thesis": "Federer-Nike era personalized sponsorship suites; post-Nike Uniqlo/On deal shows athlete equity outlasting pure endorsement — NKE benefits when athlete brands compound without scandal volatility.",
            }
        ],
        "golden_quotes": [
            "Only 54% of points won across 1,526 matches — champions move on immediately.",
            "Stress, recover, improve — Bowerman's loop Federer learned at 17.",
            "I found that person on this planet — Federer at 21 after fixing tantrums and winning Wimbledon again.",
        ],
        "chronology": {
            "subject": "Roger Federer",
            "events": [
                {"date": "Age 8–14", "event": "Junior racket abuse; boarding school at 14."},
                {"date": "Age 17", "event": "Paganini fitness; Marcoli psychology begins."},
                {"date": "2001", "event": "Wimbledon beats Sampras; fame accelerates."},
                {"date": "Age 21", "event": "Addresses tantrums; wins 21st title."},
                {"date": "2013", "event": "Forbes ~$71M highest-paid athlete."},
                {"date": "2018", "event": "Uniqlo $300M deal; On shoe investment."},
            ],
        },
    },
    "fnd-411-tortured-into-greatness-the-life-of-andre-agassi": {
        "keywords": ["NKE", "Mental Performance", "Brand Differentiation"],
        "conclusion": "Agassi's Open begins at 2006 US Open — hates tennis, cortisone shots, 869 match wins built under Mike Agassi's 2,500 daily balls. Gil Reyes and Brad Gilbert's 'win with what you have' reboot; 82-week No. 1 Sampras rivalry. Differentiation (mullet, Oakley) monetized accidentally; 1999 French Open rebirth after rock bottom. NKE stock and Oakley deals show rebel brand economics.",
        "background": "Senra covers Andre Agassi's Open — requested by listeners, central story is father Mike Agassi: 2,500 balls daily (~1 million per year), yelling everything twice, axe-handle in the car. Andre turned pro at 16 on a $1,100 check his father nearly refused; Nick Bollettieri boarding school, speed pills from brother Philly, meth at rock bottom.\n\nGil Reyes became surrogate father; Brad Gilbert coached 'ugly' pragmatic tennis — 90% consistency beats perfectionism. Won 869 matches (fifth all-time); tortured greatness against will. Brooke Shields marriage collapse, crystal meth in paparazzi era, then 1999 French Open chant 'Just get to the ball.'",
        "important_facts": [
            "Mike Agassi had Andre hit ~2,500 balls daily — ~17,500 weekly, ~1 million yearly — yelling 'harder' into his ear; Andre turned pro at 16 on a $1,100 check while father questioned 'what is money?'",
            "869 career match wins (fifth all-time) despite hating tennis; 2006 US Open opens on floor after cortisone shot — 13th career injection with vacuum-pack spine pressure before final tournament.",
            "Brad Gilbert reframed game: 90% consistency is meat-and-potatoes; perfectionism is 50% game-wise, 95% head-wise — lose 21 sets per slam if chasing perfect. 82 weeks at No. 1 rivaling Sampras; Oakley and Nike deals monetized rebel differentiation.",
        ],
        "mental_model": {
            "name": "Win With What You Have",
            "components": "Control what you control — Agassi repeats aloud in showers. Perfectionism loses 21 sets per slam; Gilbert's ugly tennis frustrates opponents with change of pace. Differentiation (look, villain arc) attracts sponsors accidentally. Rock bottom enables remade decisions — momentum from small choices.",
            "application": "Founders with obsessive parents or craft torture should externalize coaching like Gil and Brad. NKE benefited when Agassi's Oakley-shaded rebel sold product without focus-group intent — authenticity beats focus-group polish when paired with results.",
        },
        "key_insights": [
            {
                "view": "Torture can produce excellence against will.",
                "question": "How did Mike Agassi train Andre?",
                "answer": "2,500 balls daily from childhood — math to 1 million per year. Yelling twice per command; thinking labeled enemy. Andre played soccer secretly because team sport felt human — father yanked him back. Speed pills at nationals via brother Philly.",
            },
            {
                "view": "Perfectionism loses slams.",
                "question": "What did Brad Gilbert change?",
                "answer": "Honest assessment: talent exists but early aggression threatens career. Perfection is 50% game-wise, 95% head-wise — win ugly with consistency, 21 sets per slam if chasing perfect. Pocket mantra: 'Just get to the ball.'",
            },
            {
                "view": "Differentiation monetizes pain.",
                "question": "How did rebellion become brand?",
                "answer": "Mohawk, earrings, profanity fines — fans imitated look; Oakley shipped Viper and sunglasses without being asked. Villain arc satisfied shy kid's hidden craving for attention while media job ran itself.",
            },
        ],
        "top_investment_implications": [
            {
                "ticker": "NKE",
                "direction": "Watch",
                "confidence": "Low",
                "thesis": "Agassi-Nike era plus accidental Oakley amplification shows athlete rebel brands move product when differentiation is authentic — useful when evaluating NKE athlete portfolio risk/reward.",
            }
        ],
        "golden_quotes": [
            "Control what you control — Agassi repeats aloud; saying it makes him brave.",
            "2,500 balls a day — Mike Agassi's math to one million per year.",
            "Just get to the ball — Gilbert's pocket mantra through 1999 French Open rebirth.",
        ],
        "chronology": {
            "subject": "Andre Agassi",
            "events": [
                {"date": "Childhood", "event": "2,500 daily balls; Vegas casino captain father."},
                {"date": "1986", "event": "Turns pro at 16 on $1,100 check."},
                {"date": "1992", "event": "Wimbledon champion; Sampras rivalry begins."},
                {"date": "1995–1997", "event": "Peak years; marriage to Brooke Shields; meth period."},
                {"date": "1999", "event": "French Open rebirth with Gilbert."},
                {"date": "2006", "event": "Final US Open; retires on floor opening scene."},
            ],
        },
    },
    "fnd-410-excellent-advice-for-living": {
        "keywords": ["BRK.B", "Habit Formation", "Long-Term Thinking"],
        "conclusion": "Kelly's Excellent Advice for Living — 450 aphorisms from birthday batches starting at 68 — compresses Rockefeller ropes, Munger incentives, Bezos customer obsession, and Rubin redo logic. Enthusiasm worth 25 IQ points; habits beat inspiration; infinite games over finite wins. BRK.B lens via Buffett/Munger quotes Kelly channels; separate creating from improving.",
        "background": "Senra reads Kevin Kelly's Excellent Advice for Living — discovered via Instagram, read in one sitting. Kelly wrote 68 bits on his 68th birthday, continued yearly to ~450 tweetable seeds expandable into essays. Sources span Buffett, Munger, Rick Rubin, Ed Catmull, Bezos, and Rockefeller.\n\nThemes: enthusiasm and listening as superpowers; deadlines weed mediocrity; forgiveness as self-gift; measure life with your own ruler; habit ropes spun daily; hire aptitude over skills; 5% cohort power of incentives; infinite games versus finite wins; frugal except on passions.",
        "important_facts": [
            "Kelly began at 68 with 68 advice bits on his birthday, continued annually to ~450 compact aphorisms — each a seed for a longer essay, compressed from decades reading founders and thinkers.",
            "Bezos customer obsession and Munger incentive worship recur: top 5% cohort power of incentives underestimated; competing obsesses inward, customer focus pushes invention — Kelly ties to Rockefeller habit ropes spun daily until too thick to break.",
            "Catmull/Ford maternity-ward rule: separate creating from improving — editor must not kill creator; Kelly cites Ogilvy headline worth 80 cents of the dollar and rule of seven sources before believing a fact.",
        ],
        "mental_model": {
            "name": "Infinite Game Habits",
            "components": "Enthusiasm equals +25 IQ; listening is superpower. Deadlines force decisions — Nolan's creative accelerator. Build habit ropes daily; good habits hard to start, bad easy. Play infinite games with your own ruler; compound small steady gains. Separate create pass from edit pass.",
            "application": "Operators should install Kelly's rule-of-three in conversations and remove self-negotiation on hard tasks (Kobe never debated summer workouts). BRK.B shareholders benefit when managers frugal except on passions and obsess over incentives aligning behavior.",
        },
        "key_insights": [
            {
                "view": "Habits beat inspiration.",
                "question": "What is Rockefeller's rope metaphor?",
                "answer": "Kelly: spin rope daily until too thick to break — habit beats inspiration for workouts and operations. Become person who never misses workout rather than chasing mood. Munger and Buffett autobiographies show infinite-game rulers.",
            },
            {
                "view": "Create and edit separately.",
                "question": "Why protect newborn ideas?",
                "answer": "Catmull and Ford treat new work like maternity ward — editor killing creator on same pass destroys originality. Kelly separates invent/select and sketch/inspect phases; Ogilvy fought for headline time because 80 cents of dollar live there.",
            },
            {
                "view": "Customer beats competitor obsession.",
                "question": "How does Kelly echo Bezos?",
                "answer": "Obsessing competitors is inward; customer focus pushes proactive invention and durable moats. Kelly also: assume busy when emailing, try twice, then stop — high-agency people introduce themselves because everyone is shy.",
            },
        ],
        "top_investment_implications": [
            {
                "ticker": "BRK.B",
                "direction": "Watch",
                "confidence": "Low",
                "thesis": "Kelly channels Buffett/Munger on incentives, ropes, and infinite games — BRK culture of frugality except passions and candor mirrors the aphorisms' durable-business lens.",
            }
        ],
        "golden_quotes": [
            "Enthusiasm is worth 25 IQ points — Kelly's opening maxim.",
            "Spin the rope every day until too thick to break — Rockefeller via Kelly on habits.",
            "Finite games are played to win; infinite games are played to keep playing.",
        ],
        "chronology": {
            "subject": "Kevin Kelly",
            "events": [
                {"date": "Age 68", "event": "First 68 birthday advice bits to family."},
                {"date": "Annual", "event": "Birthday batches continue yearly toward ~450 aphorisms."},
                {"date": "2020s", "event": "Excellent Advice for Living published."},
                {"date": "2020s", "event": "Senra discovers book via Instagram; reads in one sitting."},
                {"date": "Ongoing", "event": "Aphorisms tie to Catmull, Rubin, Bezos, Munger, Rockefeller."},
            ],
        },
    },
    "fnd-409-the-creative-genius-of-rick-rubin": {
        "keywords": ["WMG", "Creative Process", "Differentiation"],
        "conclusion": "Rubin's The Creative Act — 78 areas of thought — pairs Wooden's sock discipline with Napoleon on neglected threads. Submerge in masterpieces; action produces information; self-doubt is not doubt in the song. Seminal works, patience, and rule-breaking differentiate — Bezos ferocious on details, Ford on money as service byproduct. WMG and labels benefit when producers protect craft from overanalysis.",
        "background": "Senra rereads Rick Rubin's The Creative Act — stream-of-consciousness across 78 brief chapters, unlike any prior Founders book. Opens with John Wooden teaching elite athletes to tie shoes — small habits compound exponentially.\n\nRubin: nothing known for certain; tune in to inner signal via walks, darkness, silence (Simons, Musk parallel). Submerge in classics not news; action before overthinking; self-doubt versus doubt-in-the-song are different; perfectionism frozen forward motion. Collaboration, intuition over intellect, and 'money is result of service' (Ford).",
        "important_facts": [
            "John Wooden made UCLA stars learn shoe-and-sock detail first — wrinkles cause blisters; Rubin cites Napoleon: great events hang on a single thread; neglect nothing.",
            "Rubin recommends darkness, silence, flat on back — Jim Simons and Elon Musk use similar void for signal; submerge in masterpieces (fine literature, cinema, architecture) instead of news to calibrate internal greatness meter.",
            "Distinction: doubting yourself versus doubting the song — former is temporary distraction, latter helpful. Rubin on Defiant Ones: many artists cannot handle success; Iovine saw smart people sabotage with pills, alcohol, megalomania at 50,000 screaming fans.",
        ],
        "mental_model": {
            "name": "Signal Through Submersion",
            "components": "Small habits (Wooden socks) compound. Create vacuum for subconscious — walks, bike, garden, fiction. Action produces information; faith without full understanding. Submerge in best works; curate inputs because environment broadcasts subtly. Break rules consciously; amplify differences not averages.",
            "application": "Product leaders should schedule empty calendar like Rubin and protect create/edit separation Kelly also preach. WMG-style catalog economics reward patient craft — impatience is argument with reality; Bezos-like ferocity on details without killing beginner mind.",
        },
        "key_insights": [
            {
                "view": "Details compound like habits.",
                "question": "Why does Rubin open with Wooden?",
                "answer": "Legendary athletes arrived expecting drills; Wooden taught sock wrinkles cause blisters — each small habit exponential across season. Napoleon parallel: clever man neglects nothing hanging on single thread.",
            },
            {
                "view": "Void summons signal.",
                "question": "How do Rubin, Simons, and Musk align?",
                "answer": "Quiet dark room, flat, no inputs for an hour — subconscious floods when overpacked mind empties. Rubin walks, bikes, swims; news discarded for classics to hone sensitivity to greatness.",
            },
            {
                "view": "Doubt the work, not the self.",
                "question": "What kills artists after success?",
                "answer": "Rubin via Iovine: overdose, pills, megalomania when 50,000 fans scream your name — self-sabotage from unhealthy self-image. Doubting the song helps; doubting yourself procrastinates. Gratitude tips balance.",
            },
        ],
        "top_investment_implications": [
            {
                "ticker": "WMG",
                "direction": "Watch",
                "confidence": "Low",
                "thesis": "Rubin's producer economics — patience, differentiation, service-first — mirror durable catalog value; labels win when craft protected from overanalysis and artists avoid success-sabotage cycles.",
            }
        ],
        "golden_quotes": [
            "The person you're competing against is yourself — Rubin after Wooden.",
            "Action produces information — move before overthinking reveals next step.",
            "Money is the result of service — Henry Ford via Rubin's closing frame.",
        ],
        "chronology": {
            "subject": "Rick Rubin",
            "events": [
                {"date": "1980s", "event": "Def Jam founding; LL Cool J, Beastie Boys era."},
                {"date": "1990s–2000s", "event": "Producer across genres; American Recordings."},
                {"date": "Episode 245", "event": "Prior Founders biography episode."},
                {"date": "2020s", "event": "The Creative Act published — 78 areas of thought."},
                {"date": "Ongoing", "event": "Tetragrammaton; professional listener craft."},
            ],
        },
    },
    "fnd-407-bruce-springsteen-repairs-the-hole-in-himself": {
        "keywords": ["SONY", "Creative Endurance", "Brand Trust"],
        "conclusion": "Born to Run memoir — ~600 pages handwritten twice — maps Bruce's relentless ethic, benevolent E Street dictatorship, and depression repair. Elvis 1956 earthquake, Born to Run 1975, Columbia flop then arena fill, 3,000+ shows, 150M+ records. Iovine taught work ethic; customer trust compounds decades touring. SONY/music majors lens: authenticity and endurance beat flash supernovas.",
        "background": "Senra reads Bruce Springsteen's Born to Run after months avoiding the emotional weight — Bruce articulates work feelings Senra could not. Defiant Ones friendship with Jimmy Iovine: Bruce wanted to be great, not merely rich or famous.\n\nHandwrote ~600 pages twice for tone. Childhood kerosene heat, silent father, Elvis and Beatles earthquakes, Steel Mill to E Street Band. Signed benevolent dictatorship — clarity over democracy. Depression, Patty Scialfa repair, 3,000 concerts, longevity obsession with John Landau.",
        "important_facts": [
            "Springsteen handwrote ~600-page Born to Run twice for tone — relentless ethic from nearly 70-year-old man; Iovine in Defiant Ones: Bruce wanted greatness, not just fame or money.",
            "Elvis on TV called 'human earthquake' at 15; Born to Run 1975 breakthrough after years filling 7 C's sweat — 3,000+ concerts; Howard Stern notes 150M+ records and Rock Hall despite breaking family chains.",
            "Early Columbia Records flop nearly broke band — $3,000 contract split left ~$3 per member; rebuilt playing parks, armories, supermarkets. 2010s still selling stadiums — fan trust compounded 80+ years; Ramp-style detail obsession on costs parallels Bruce's penny discipline on touring.",
        ],
        "mental_model": {
            "name": "Repair the Hole With Work",
            "components": "Childhood hole from silent raging father fuels relentless pursuit — 'If not furious by nightfall, quit burning.' Benevolent dictatorship: creative input welcome, structure prepared. Longevity over supernova — endurance, durability, intelligence beat initial instinct. Depression channeled through music and therapy, not chemicals.",
            "application": "Consumer brands (SONY catalog, live promoters) reward artists who tour with sweat equity decades — Bruce's fan trust is moat flash acts lack. Founders should handwritten-edit tone on flagship products; democracy kills urgent craft.",
        },
        "key_insights": [
            {
                "view": "Greatness requires relentless ethic.",
                "question": "What did Iovine teach Bruce?",
                "answer": "Defiant Ones: Bruce didn't want to be rich or famous — happy via greatness. Relentlessly determined when pushing frontiers; surround with believers or exhaust them. Handwrote 600 pages twice — pour love into details customers feel.",
            },
            {
                "view": "Dictatorship can be benevolent.",
                "question": "How did E Street Band govern?",
                "answer": "Clarity ruled — benevolent dictatorship with welcomed creative input but prepared structure. Failed democracy stopped Steel Mill; $3 per member after $3,000 deal taught financial clarity. Bruce assumed decision-making to follow muse without endless argument.",
            },
            {
                "view": "Endurance beats supernova.",
                "question": "Why prioritize durability?",
                "answer": "Rock favors flash burnout; Bruce and Landau chose lifeline touring — 3,000 shows, sweat-drenched catharsis. Aging scary but morphs enlightening; prioritize breathing number of days creating over one brilliant dying supernova.",
            },
        ],
        "top_investment_implications": [
            {
                "ticker": "SONY",
                "direction": "Watch",
                "confidence": "Low",
                "thesis": "Springsteen catalog on Columbia/Sony lineage shows long-horizon music economics — touring and trust compound when authenticity replaces flash; useful lens for major-label durable cash flows.",
            }
        ],
        "golden_quotes": [
            "I didn't want to be rich or famous — I wanted to be great — Bruce via Iovine.",
            "If by end of night you're not furious, quit burning — Bruce's work ethic test.",
            "Only the luckiest grow apart — everyone else moves differently with same commitment.",
        ],
        "chronology": {
            "subject": "Bruce Springsteen",
            "events": [
                {"date": "1956", "event": "Elvis on TV — human earthquake at 15."},
                {"date": "1960s", "event": "Steel Mill; E Street Band forms."},
                {"date": "1972", "event": "Columbia Records debut — initial flop."},
                {"date": "1975", "event": "Born to Run breakthrough."},
                {"date": "1980s–90s", "event": "Depression, marriages, therapy arc."},
                {"date": "2016+", "event": "Born to Run memoir published; Broadway run."},
            ],
        },
    },
    "fnd-406-christian-von-koenigsegg": {
        "keywords": ["Private:Koenigsegg", "Vertical Integration", "Hypercar Engineering"],
        "conclusion": "Von Koenigsegg founded at 22 in 1994 with no auto background — CC8S took eight years; Paris 2002 reveal after grants, father bridge loan, and pen-trading in post-Soviet Baltics. ~600 staff, thousand parts in-house, Guinness speed records, 287 mph. Private:Koenigsegg compounds vertical integration, 'challenges not problems,' and autotelic craft like Dyson.",
        "background": "Senra studied Christian von Koenigsegg after Daniel Ek's recommendation — Spotify founder guest — plus documentary deep dive. At five, Norwegian stop-motion film Flåklypa Grand Prix inspired build-your-own-race-car dream. Founded August 12, 1994 at 22 with no engineering degree; CC8S prototype took until 2002 Paris Auto Show.\n\nEight-year struggle 1994–2002 funded by speeches, Swedish grants, father's retirement loan, and teenage pen/plastic-bag/frozen-chicken trades in Estonia. Factory fire, decommissioned airbase move, in-house engine when no supplier existed. Munger-style indifference to troubles; weight equals cost mantra.",
        "important_facts": [
            "Founded Koenigsegg August 12, 1994 at age 22 — no engineering or manufacturing background; CC8S prototype took eight years until 2002 Paris Auto Show reveal after grants, father bridge loan, and seminar income.",
            "1990s post-Soviet trade: sold pens, plastic bags, frozen chicken to Baltics — 'odd jobs towards true passion since age five.' Factory fire on thatched-roof farm; moved to decommissioned Swedish air force hangar with jet-squadron runway testing.",
            "~600 employees, ~1,000 parts manufactured in-house — von Koenigsegg bought Tesla IPO shares; weighs every nut/bolt because decrease weight equals decrease cost/revenue analog; Guinness records include 287 mph and 250+ speed records.",
        ],
        "mental_model": {
            "name": "Challenges Not Problems",
            "components": "Rename problems challenges — forward motion never stops. Vertical integration when budgets forbid suppliers (custom V8 when none existed). Autotelic craft: build for building's sake like Founders podcast name worst but meaningful. Labor-intensive small batch adapts faster than heritage giants.",
            "application": "Private hypercar moat is in-house engine, carbon prep from F1/jets, and storytelling selling sight-unseen — buyers fund R&D. Founders at 22 should start experimenting like Jeremy Fry mentored Dyson: action produces information, not business plans alone.",
        },
        "key_insights": [
            {
                "view": "Start absurdly early with no credentials.",
                "question": "How did Koenigsegg begin at 22?",
                "answer": "August 12, 1994 — no auto experience, limited funding, lifelong obsession since age five. Truck-driver neighbor and Volvo engineer on drawing table; modeled CC8S without computers until 1997–98. Eight-year void funded by speeches and father's retirement.",
            },
            {
                "view": "Integrate when suppliers fail.",
                "question": "Why build engines in-house?",
                "answer": "Needed engine more powerful than any existing manufacturer; budgets limited. Now ~1,000 parts in-house — wheels, calipers, seats, software, cloud connectivity. Weight reduction equals cost reduction — nut/bolt scale obsessively.",
            },
            {
                "view": "Motion beats panic.",
                "question": "What is 'challenges not problems'?",
                "answer": "Materials fail, prototypes break, suppliers bankrupt — expect imperfection, pivot instantly. Factory fire became airbase move with runway testing advantage. Relentless forward motion under chaos; Munger: indifference to troubles inescapable in life.",
            },
        ],
        "top_investment_implications": [
            {
                "ticker": "Private:Koenigsegg",
                "direction": "Watch",
                "confidence": "Medium",
                "thesis": "Vertically integrated hypercar with Guinness speed proof and sight-unseen marketing — compounding craft moat without public float; Tesla IPO stake shows public-market learning appetite.",
            }
        ],
        "golden_quotes": [
            "Challenges, not problems — Koenigsegg cultural motto when prototypes break.",
            "Decrease weight, decrease cost — every nut weighed like revenue on the scale.",
            "Build for the sake of building — autotelic craft since age five.",
        ],
        "chronology": {
            "subject": "Christian von Koenigsegg",
            "events": [
                {"date": "Age 5", "event": "Flåklypa Grand Prix inspires car-building dream."},
                {"date": "1994-08-12", "event": "Koenigsegg Automotive founded at age 22."},
                {"date": "1994–2002", "event": "Eight-year prototype struggle; Baltics trade income."},
                {"date": "2002", "event": "CC8S revealed Paris Auto Show."},
                {"date": "2000s", "event": "Factory fire; air force hangar move."},
                {"date": "2020s", "event": "~600 staff; 287 mph; 250+ Guinness records."},
            ],
        },
    },
    "fnd-397-jiro-ono-simplicity-is-the-ultimate-advantage": {
        "keywords": ["Private:Jiro", "Kaizen", "Operational Excellence"],
        "conclusion": "Jiro Dreams of Sushi — 75 years same job, 10-seat subway counter, three Michelin stars at 82 after decades invisible fame. Ultimate simplicity: $400/person (~$25/minute), tuna-only vendors, 40-minute octopus massage, 200 rejected egg iterations. Private:Jiro shows shokunin kaizen beats scale — differentiation via subtraction like Dyson and Disney detail checks.",
        "background": "Senra transcribed the Jiro documentary — Jiro Ono at 85 in film, 75 years same occupation. Shokunin craftsman: moral duty to perfect craft for society, not ego. Ten-seat Tokyo subway station restaurant; reservations mandatory; no appetizers — sushi only.\n\nKaizen daily routine: same train seat, dislikes holidays. Apprentices start at 19 — hot towels burn hands before touching fish; 200 egg iterations. Rice dealer with pressure-cooker rivals; octopus massaged 40–50 minutes. Three stars at 82; younger son two stars at mirror restaurant.",
        "important_facts": [
            "Jiro: 75 years same job; 10-seat counter in Tokyo subway; ~$400 per person (~60,000 yen today), ~15–20 minute meal — roughly $25/minute, no appetizers, sushi only.",
            "Apprenticeship gauntlet: hot towels burn hands before cutting fish; egg cooking requires 200 iterations until 'now you are done' — opened own shop at 39 after decades; three Michelin stars at 82.",
            "Octopus massaged 40–50 minutes for softness; tuna vendor sells only tuna — specialists per ingredient; rice dealer uses pressure cooker water at body temperature for ideal deliciousness moment.",
        ],
        "mental_model": {
            "name": "Ultimate Simplicity (Shokunin)",
            "components": "Novice spotted by too much — master uses fewest resources for intention. Kaizen: same routine daily; taste before every serve. Specialists per ingredient; anti-establishment rebel buys best, no compromise. Details are product — Disney/Main Street parity.",
            "application": "Luxury and craft businesses win by subtraction not addition — Ferrero, Ferrari, Jiro share impatience with uncleanliness and detail checks. Private operators should reject scale that breaks routine; reservations and price filter serious customers.",
        },
        "key_insights": [
            {
                "view": "Simplicity is competitive moat.",
                "question": "What is ultimate simplicity?",
                "answer": "Master chefs ask how Jiro achieves depth with such simple presentation — answer: purity via subtraction. Novice uses too many ingredients and movements; master uses minimum for intention. Tiny subway ten-seat counter beats hundreds of Tokyo rivals.",
            },
            {
                "view": "Routine is the product.",
                "question": "How does Jiro treat holidays?",
                "answer": "Dislikes holidays — wants routine back immediately. Same train seat daily; countless tastings/experiments per day. If it doesn't taste good, can't serve it — self-critical inner monologue like history's greatest entrepreneurs.",
            },
            {
                "view": "Apprenticeship is gauntlet.",
                "question": "How are apprentices trained?",
                "answer": "Hot towels burn hands before fish; years cleaning only; 200 egg iterations rejected. Jiro started at nine after homeless bridge childhood — failure not option. Specialists supply tuna-only, octopus-only; 40-minute massage exemplifies shokunin quality.",
            },
        ],
        "top_investment_implications": [
            {
                "ticker": "Private:Jiro",
                "direction": "Watch",
                "confidence": "Medium",
                "thesis": "Shokunin model — price per minute, zero scale compromise, supplier specialization — is benchmark for private luxury craft; Raising Cane's one-menu focus and LVMH detail culture rhyme.",
            }
        ],
        "golden_quotes": [
            "Ultimate simplicity leads to purity — master chefs on Jiro's depth.",
            "If it doesn't taste good, you can't serve it — daily tasting mantra.",
            "Once you decide your occupation, immerse and fall in love — 75 years same job.",
        ],
        "chronology": {
            "subject": "Jiro Ono",
            "events": [
                {"date": "Age 9", "event": "Leaves home; bridge survival; craft as lifeline."},
                {"date": "Age 19", "event": "Apprenticeship begins — hot towel gauntlet."},
                {"date": "Age 39", "event": "Opens own ten-seat restaurant."},
                {"date": "Age 82", "event": "Three Michelin stars awarded."},
                {"date": "Film era", "event": "Jiro Dreams of Sushi documentary at ~85."},
                {"date": "Ongoing", "event": "Younger son two-star mirror restaurant; kaizen daily."},
            ],
        },
    },
}
