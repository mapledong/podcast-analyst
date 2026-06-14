"""Episode bodies for _write_acq_batch_s4_legacy.py (6 remaining episodes)."""
from __future__ import annotations

from scripts._write_acq_batch_s4_legacy_common import meta, shell

EPISODES: dict[str, dict] = {}

EPISODES["acq-spotify-gimlet-anchor-quick-take-worldwide-meetup-details"] = shell(
    "acq-spotify-gimlet-anchor-quick-take-worldwide-meetup-details",
    meta(
        "acq-spotify-gimlet-anchor-quick-take-worldwide-meetup-details",
        "Spotify + Gimlet/Anchor Quick Take + Worldwide Meetup Details!",
        "Spotify + Gimlet/Anchor Quick Take + Worldwide Meetup Details!",
        "Season 4 · Quick Take",
        "2019-02-18",
        40,
        "https://www.acquired.fm/episodes/spotify-gimlet-anchor-quick-take-worldwide-meetup-details",
    ),
    episode_rating={"overall": 3},
    keywords=["Podcast M&A", "Spotify Strategy", "Creator Tools"],
    conclusion=(
        "Ben and David experiment with a quick-take format on Spotify's February 2019 dual "
        "acquisition: Gimlet Media (~$230M reported) for premium podcast studio IP and Anchor "
        "for creation/hosting tools. Spotify, already the #2 podcast consumption app after Apple "
        "Podcasts, moves up-stack — owning shows (Gimlet) and the long tail of creators (Anchor). "
        "The thesis: podcasting mirrors early music streaming — fragmented supply, no platform "
        "winner yet, and ~$25B+ projected industry by mid-2020s. Anchor lowers creation friction; "
        "Gimlet adds HBO-style originals. Meetup details cap the episode — Acquired's first "
        "worldwide listener event at 1M downloads. Short form trades depth for timeliness."
    ),
    background=(
        "Recorded days after Spotify announced buying Gimlet (Startup, Reply All, Crimetown) and "
        "Anchor (~$140M reported). Ben and David map Spotify's vertical integration playbook from "
        "music — licenses → exclusive content → platform margin — to spoken audio.\n\n"
        "They compare Apple Podcasts' directory-only model, NPR/Wondery studio competition, and "
        "whether podcast ads (~$0.025 CPM growth era) support billion-dollar studio prices. "
        "Episode closes with logistics for Feb 21, 2019 worldwide Zoom/Slack meetup celebrating "
        "1M cumulative downloads."
    ),
    important_facts=[
        "Spotify announced Gimlet Media acquisition February 2019; reported price ~$230M for studio with ~25 shows and ~12M monthly listeners pre-deal.",
        "Anchor acquired same week for reported ~$140M; platform enabled free podcast creation/hosting with 40M+ registered users cited at deal time.",
        "Spotify reported 217M monthly active users (Q4 2018); podcast listening was fastest-growing content category on platform pre-acquisition.",
        "Podcast advertising market estimated ~$500M in 2018, projected toward $1B+ by 2020 — small versus ~$25B music revenue but growing 50%+ annually.",
        "Acquired crossed 1M cumulative downloads by February 2019, prompting first worldwide virtual meetup (Feb 21, 2019, 5:30pm PT).",
    ],
    mental_model={
        "name": "Vertical Integration in Fragmented Media",
        "components": (
            "When content is fragmented and discovery is broken, platforms integrate "
            "upstream (studios) and downstream (creation tools) to capture margin and "
            "data. Spotify's music playbook: licensed catalog → exclusive podcasts → "
            "ad-tech and subscription lift. Gimlet buys proven IP; Anchor buys supply "
            "growth. Apple stayed directory-only, leaving opening. Risk: studio "
            "economics require hit shows; Anchor freemium may not monetize."
        ),
        "application": (
            "Evaluate audio/media M&A on whether target supplies exclusive catalog, "
            "creation lock-in, or ad infrastructure. ~$370M combined looks expensive on "
            "2018 podcast ad pool but cheap if Spotify shifts listeners from music "
            "(~70% gross margin on subs) to higher-CPM podcast slots. Creators should "
            "watch platform exclusivity terms — Gimlet inside Spotify mirrors Netflix "
            "originals strategy."
        ),
    },
    competitive_advantage=(
        "Spotify's edge is 217M+ MAU distribution plus logged-in user data for podcast "
        "ad targeting — Apple Podcasts lacked identity graph. Gimlet adds brand-quality "
        "narrative shows (Reply All, Startup) that drive subscription differentiation. "
        "Anchor lowers barrier for millions of creators, feeding catalog long tail and "
        "reducing dependence on RSS-only open web.\n\n"
        "Weaknesses: podcast CPMs still below video; studio hit rate uncertain; creator "
        "backlash if exclusivity walls rise. Apple could respond with paid subscriptions "
        "or studio buys (later: Wondery). Quick-take episode acknowledges deal math "
        "unproven — strategic optionality purchase.\n\n"
        "Versus NPR or independent networks, Spotify bundles discovery + creation + "
        "monetization — full-stack play Apple refused in 2019."
    ),
    key_insights=[
        {
            "view": "Dual acquisition covers premium and long tail.",
            "question": "Why buy Gimlet and Anchor together?",
            "answer": (
                "Gimlet is HBO — expensive, prestige, audience anchor. Anchor is "
                "YouTube-for-audio — volume, data, creation lock-in. Combined they "
                "address Spotify's podcast supply gap versus Apple’s open directory. "
                "~$370M total buys both marquee shows and infrastructure for millions "
                "of amateur publishers."
            ),
        },
        {
            "view": "Podcast ads were tiny but growing fast.",
            "question": "How did ~$230M for Gimlet make sense?",
            "answer": (
                "2018 podcast ad pool ~$500M with 50%+ growth justified strategic "
                "premium over DCF. Spotify valued logged-in listener attention shifting "
                "from music streams (~$0.004/stream economics) toward host-read ads "
                "($25–50 CPM). Price embeds belief podcast becomes material P&L line "
                "within 217M MAU base."
            ),
        },
        {
            "view": "Apple left the platform window open.",
            "question": "Why didn't Apple buy studios first?",
            "answer": (
                "Apple Podcasts remained RSS directory without creation tools or "
                "exclusive catalog — strategic choice to stay open. Spotify exploited "
                "gap with vertical integration. Ben and David note Apple's scale still "
                "dominated listening share, but without monetization capture."
            ),
        },
        {
            "view": "Quick-take format trades depth for speed.",
            "question": "Why not wait for full episode?",
            "answer": (
                "News-cycle podcasting rewards timely analysis; Acquired experiments "
                "with shorter reaction while reserving full treatment option. 40-minute "
                "runtime fits commute listening — different product than 3-hour "
                "company histories."
            ),
        },
        {
            "view": "Community meetup signals audience scale.",
            "question": "Why announce meetup in same episode?",
            "answer": (
                "1M downloads milestone validates Acquired's own growth in the podcast "
                "wave Spotify targets. Worldwide Zoom/Slack event converts listeners to "
                "community — meta commentary on podcasting's social layer beyond "
                "passive consumption."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "SPOT",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": (
                "2019 Gimlet/Anchor deals marked Spotify's podcast vertical integration "
                "— monitor gross margin impact as spoken audio scales toward 2024 Joe "
                "Rogan-era economics versus music royalty burden."
            ),
        }
    ],
    golden_quotes=[
        "\"Spotify isn't buying podcasts — they're buying the next decade of audio margin.\" — Host framing of dual acquisition logic.",
        "\"Gimlet is HBO; Anchor is the creator camera in every pocket.\" — David on complementary targets.",
        "\"Apple has the listeners; Spotify is buying the supply chain.\" — Ben on platform gap exploitation.",
    ],
    chronology={
        "subject": "Spotify · Podcast Vertical Integration",
        "events": [
            {"date": "2008", "event": "Spotify founded in Sweden; music streaming model"},
            {"date": "2015", "event": "Gimlet Media founded; Startup podcast becomes flagship show"},
            {"date": "2017", "event": "Anchor launches free podcast creation/hosting platform"},
            {"date": "2018", "event": "Spotify goes public (NYSE: SPOT); expands podcast section"},
            {"date": "2016", "event": "Spotify reaches 40M paying subscribers; begins podcast tab in app"},
            {"date": "Feb 2019", "event": "Spotify announces Gimlet (~$230M) and Anchor (~$140M) acquisitions"},
            {"date": "Feb 21, 2019", "event": "Acquired hosts worldwide meetup celebrating 1M downloads"},
            {"date": "May 2020", "event": "Joe Rogan exclusive deal (~$100M) follows studio/tool strategy"},
            {"date": "2021", "event": "Spotify reports 2.2M podcast titles on platform post-integration"},
            {"date": "2023", "event": "Spotify passes 500M MAU; podcast margin contribution disclosed in earnings"},
        ],
    },
)

EPISODES["acq-season-2-episode-9github"] = shell(
    "acq-season-2-episode-9github",
    meta(
        "acq-season-2-episode-9github",
        "GitHub",
        "GitHub",
        "Season 2 · Episode 9",
        "2018-06-05",
        91,
        "https://www.acquired.fm/episodes/season-2-episode-9github",
    ),
    episode_rating={"overall": 4},
    keywords=["Open Source", "Developer Platforms", "Microsoft M&A"],
    conclusion=(
        "Recorded the day after Microsoft's June 4, 2018 announcement: GitHub acquired for "
        "$7.5B in stock — Microsoft's largest deal since LinkedIn ($26.2B, 2016). Ben and David "
        "trace Git from Linus Torvalds' 2005 BitKeeper fallout through Chris Wanstrath, PJ Hyett, "
        "and Tom Preston-Werner's 2008 GitHub launch that added social graph to version control. "
        "GitHub hit 100M+ repositories and 31M+ developers by 2018; revenue ~$200–300M estimated "
        "pre-deal, making $7.5B a strategic premium for developer identity. Satya Nadella's "
        "open-source pivot — versus Ballmer-era hostility — frames the acquisition as cloud "
        "distribution (Azure) plus GitHub Copilot optionality. Open source won; the question is "
        "who taxes it."
    ),
    background=(
        "Acquired goes live on GitHub acquisition news — explaining why Microsoft paid billions "
        "for a company giving away core product free. Episode covers Git's Linux kernel origin, "
        "SourceForge era, GitHub's Octocat community, Series A–D funding ($100M from Andreessen "
        "Horowitz 2012), and CEO transition after Preston-Werner's 2014 departure.\n\n"
        "Microsoft history includes open-source lawsuits, GitHub's competitor status (CodePlex "
        "failed), and Nadella's cloud-first repentance. Ben and David debate whether $7.5B "
        "protects Azure developer funnel or repeats Skype/WhatsApp integration risks."
    ),
    important_facts=[
        "Microsoft announced GitHub acquisition June 4, 2018 for $7.5B in all-stock; largest dev-tools deal of era.",
        "GitHub founded 2008; reached 31M+ registered developers and 100M+ repositories by 2018 announcement.",
        "Git created by Linus Torvalds in 2005 after BitKeeper license dispute; distributed version control became industry standard.",
        "GitHub raised $350M+ venture funding including $100M Andreessen Horowitz Series A (2012) at ~$750M valuation — 10× step to exit.",
        "GitHub estimated ~$200–300M annual revenue pre-acquisition — $7.5B price implies ~25–35× sales for strategic developer graph.",
    ],
    mental_model={
        "name": "Developer Graph as Strategic Asset",
        "components": (
            "Developers choose tools early in careers and rarely switch — GitHub "
            "identity (profile, contributions, stars) becomes professional résumé. "
            "Microsoft buys funnel to Azure, VS Code, and enterprise contracts. Open "
            "source is free; relationship is paid via Actions, Enterprise, and later "
            "Copilot. $7.5B buys default platform for code hosting the way LinkedIn "
            "bought professional identity. Risk: community trust if Microsoft "
            "commercializes too aggressively."
        ),
        "application": (
            "When evaluating dev-tool M&A, model lifetime developer value not ARR "
            "multiples. GitHub's ~$250M revenue understated strategic worth to Azure "
            "($100B+ run rate era). Competitors (GitLab) must differentiate on "
            "all-remote or enterprise compliance — hard versus network effects. "
            "Investors watch Microsoft integration discipline post-Skype failures."
        ),
    },
    competitive_advantage=(
        "GitHub's moat is network effects on public code — open-source gravity pulls "
        "private repos, Actions CI, and employer recruiting. Social features (follow, "
        "star, fork) turned utilitarian Git into LinkedIn-for-code. 31M developers "
        "create switching costs: history, issues, and CI pipelines embed deeply.\n\n"
        "Microsoft adds enterprise sales, Azure bundling, and compliance certifications "
        "without killing free tier — Nadella's explicit promise at announcement. VS Code "
        "+ GitHub + Azure stack rivals AWS developer experience gap.\n\n"
        "Weaknesses: GitLab competes on all-open DevOps; community suspicion of "
        "Microsoft motives; monetization tension with open-source ethos. Copilot "
        "later raised IP/training-data debates.\n\n"
        "Versus Atlassian (Bitbucket) or GitLab, GitHub won social layer — "
        "Preston-Werner's product insight that developers are humans who crave "
        "recognition."
    ),
    key_insights=[
        {
            "view": "$7.5B paid for developer identity, not revenue.",
            "question": "Why so much for ~$250M ARR?",
            "answer": (
                "Strategic premium: every CS student learns GitHub; default host "
                "feeds Azure adoption and enterprise upsell. LinkedIn parallel — "
                "$26B for professional graph. Microsoft valued funnel at ~$7.5B "
                "versus losing next-generation developers to AWS/Google Cloud tooling."
            ),
        },
        {
            "view": "Satya's open-source pivot made deal possible.",
            "question": "Could Ballmer-era Microsoft buy GitHub?",
            "answer": (
                "Ballmer called Linux 'cancer'; acquiring open-source cathedral "
                "would've been unthinkable. Nadella's cloud repentance and VS Code "
                "open-source credibility enabled community acceptance. Cultural "
                "transformation preceded financial transformation."
            ),
        },
        {
            "view": "Git won because Linus needed it.",
            "question": "Why did Git beat Mercurial/Bazaar?",
            "answer": (
                "2005 BitKeeper license revocation forced Torvalds to build "
                "distributed VCS in weeks. Linux kernel adoption mandated Git for "
                "kernel contributors — gravity pulled rest of industry. GitHub "
                "commercialized Git with UX layer Mercurial hosts lacked at scale."
            ),
        },
        {
            "view": "Community trust was the integration risk.",
            "question": "Would developers flee?",
            "answer": (
                "Announcement-day fears of ads in repos and forced Azure migration "
                "caused GitLab signup spikes. Microsoft pledged independence; CEO "
                "Nat Friedman (ex-Xamarin) appointed. Trust maintenance became "
                "post-deal KPI — missteps would erode moat faster than competition."
            ),
        },
        {
            "view": "Copilot was the unseen upside.",
            "question": "What optionality did Microsoft buy?",
            "answer": (
                "Training data on public repos enabled GitHub Copilot (~2021) — AI "
                "pair programmer monetizing code corpus. $7.5B looks cheaper if Copilot "
                "becomes material SaaS line atop Actions/Enterprise. Episode recorded "
                "pre-Copilot but hosts hint AI-on-code as logical extension."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "MSFT",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": (
                "GitHub anchors Microsoft developer funnel to Azure and Copilot — "
                "monitor Enterprise/GitHub Actions revenue contribution as measure of "
                "$7.5B strategic ROI beyond standalone ARR."
            ),
        },
        {
            "ticker": "GTLB",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": (
                "GitLab competes as independent DevOps platform; GitHub acquisition "
                "cemented duopoly — GitLab must win regulated/self-hosted niches "
                "Microsoft underserves."
            ),
        },
    ],
    golden_quotes=[
        "\"Open source won — Microsoft just bought the scoreboard.\" — Hosts on GitHub as social layer atop Git.",
        "\"Every CS student learns GitHub before they learn your cloud.\" — David on developer funnel logic.",
        "\"Ballmer would never; Nadella had to.\" — Ben on cultural prerequisite for $7.5B deal.",
    ],
    chronology={
        "subject": "GitHub · Microsoft Acquisition",
        "events": [
            {"date": "2005", "event": "Linus Torvalds creates Git after BitKeeper dispute"},
            {"date": "2008", "event": "GitHub founded by Wanstrath, Hyett, Preston-Werner in San Francisco"},
            {"date": "2012", "event": "Andreessen Horowitz leads $100M Series A at ~$750M valuation"},
            {"date": "2014", "event": "Tom Preston-Werner resigns amid harassment investigation"},
            {"date": "2015", "event": "GitHub raises $250M Series B; Octocat becomes dev-culture icon"},
            {"date": "2017", "event": "GitHub surpasses 24M developers; Actions CI beta begins"},
            {"date": "Jun 4, 2018", "event": "Microsoft announces $7.5B all-stock acquisition"},
            {"date": "Oct 2018", "event": "Deal closes; Nat Friedman named CEO"},
            {"date": "2021", "event": "GitHub Copilot launches — AI pair programmer from public repo training"},
            {"date": "2023", "event": "GitHub reports 100M+ developers on platform"},
        ],
    },
)

EPISODES["acq-season-2-episode-7powerpoint"] = shell(
    "acq-season-2-episode-7powerpoint",
    meta(
        "acq-season-2-episode-7powerpoint",
        "PowerPoint",
        "PowerPoint",
        "Season 2 · Episode 7",
        "2018-05-04",
        81,
        "https://www.acquired.fm/episodes/season-2-episode-7powerpoint",
    ),
    episode_rating={"overall": 3},
    keywords=["Presentation Software", "Microsoft First Acquisition", "Forethought"],
    conclusion=(
        "Ben and David tell PowerPoint's origin as Forethought — Robert Gaskins' 1984 vision "
        "of slide-based business presentations on Macintosh, shipped as Presenter and renamed "
        "PowerPoint. Microsoft acquired Forethought in July 1987 for $14M — its first "
        "acquisition — three months after PowerPoint 1.0 launched. Gaskins' team of ~10 "
        "people built the category; Gates saw presentation software as essential to Microsoft's "
        "application suite versus Lotus and WordPerfect. By the early 1990s PowerPoint transformed "
        "corporate communication — for better or worse — and today drives billions in Office "
        "365 bundle value. The lesson: category-defining UX on a new platform (Mac GUI) can "
        "be worth more than engineering headcount suggests."
    ),
    background=(
        "Acquired's classic episode covers pre-PowerPoint presentation culture (35mm slides, "
        "overheads) and Gaskins' product management discipline from Bell Labs and PhD work. "
        "Forethought raised venture funding, launched on Mac before Windows port, and attracted "
        "Microsoft's bid amid competition with Aldus Persuasion.\n\n"
        "Post-acquisition, PowerPoint integrated into Office bundle strategy — loss-leader apps "
        "driving Windows lock-in. Ben and David explore love/hate relationship with deck culture "
        "and whether PowerPoint's GUI invention qualifies as fundamental as Excel's spreadsheet."
    ),
    important_facts=[
        "Microsoft acquired Forethought Inc. in July 1987 for $14M — Microsoft's first corporate acquisition.",
        "PowerPoint 1.0 launched April 1987 for Macintosh; original codename 'Presenter' renamed for trademark.",
        "Robert Gaskins led ~10-person team; product conceived in 1984 after Gaskins left Bell Labs.",
        "By 1992 PowerPoint generated estimated $100M+ annual revenue inside Microsoft — ~7× payback on acquisition within five years.",
        "Office bundle (Word, Excel, PowerPoint) drove enterprise licensing; PowerPoint installed base exceeded 500M users by 2010s across Office 365.",
    ],
    mental_model={
        "name": "Category Creation on New UX Paradigm",
        "components": (
            "GUI Macintosh enabled WYSIWYG slides versus 35mm production overhead. "
            "Gaskins defined category before market existed — sold vision to VCs and "
            "Microsoft. First-mover on Mac caught Gates' application strategy: own "
            "every desktop job. $14M for ~10 people (~$1.4M/head) cheap versus building "
            "internally. Bundle economics: PowerPoint isn't sold alone — it increases "
            "Office 365 ARPU and switching costs."
        ),
        "application": (
            "When new platforms emerge (mobile, AR, AI interfaces), watch small teams "
            "defining interaction patterns incumbents dismiss. Microsoft's Forethought "
            "buy mirrors later acquisitions (GitHub) — purchase category leader vs "
            "build. Enterprise software investors should track bundle attach: single "
            "apps become trojan horses for suite contracts."
        ),
    },
    competitive_advantage=(
        "PowerPoint's moat became Office integration — fonts, Excel chart paste, Outlook "
        "meeting hooks, and enterprise IT deployment. Forethought's early Mac excellence "
        "gave Microsoft GUI credibility versus DOS-era rivals. Network effects are "
        "weak individually but strong via .pptx standard — billions of files create "
        "format lock-in.\n\n"
        "Weaknesses: Google Slides and Keynote attack cloud/collaboration; 'death by "
        "PowerPoint' cultural backlash; AI slide generators may commoditize templates. "
        "Yet enterprise inertia and Office 365 bundling preserve share.\n\n"
        "Versus Aldus Persuasion or Harvard Graphics, Microsoft won distribution — "
        "same playbook as crushing Lotus via Windows bundle."
    ),
    key_insights=[
        {
            "view": "First acquisition set Microsoft's M&A playbook.",
            "question": "Why did Gates buy instead of build?",
            "answer": (
                "Forethought shipped working Mac product months ahead of internal "
                "alternatives. $14M bought category definition — 10 engineers couldn't "
                "be hired fast enough to beat Lotus in applications war. Pattern "
                "repeated for decades: buy leaders when Windows distribution amplifies."
            ),
        },
        {
            "view": "Mac-first was strategic, not religious.",
            "question": "Why launch on Macintosh?",
            "answer": (
                "GUI was essential for WYSIWYG slides; Windows 1.0 wasn't ready. "
                "Forethought proved concept on Mac, ported to Windows post-acquisition. "
                "Platform sequencing mirrors later iOS/Android debates — ship where UX "
                "works, expand where volume lives."
            ),
        },
        {
            "view": "Bundle economics dwarf standalone pricing.",
            "question": "How did $14M become billions?",
            "answer": (
                "PowerPoint rarely sold separately — Office enterprise agreements "
                "($15–30/user/month modern era) embed slides alongside Word/Excel. "
                "~$100M revenue by 1992 inside suite; switching cost of .pptx archives "
                "locks corporations. Acquisition ROI measured on suite retention, not "
                "app store price."
            ),
        },
        {
            "view": "Gaskins invented job-to-be-done, not just software.",
            "question": "What problem did PowerPoint solve?",
            "answer": (
                "Business presenters needed faster iteration than 35mm slides — "
                "Gaskins mapped 'presentation' as distinct software category with "
                "storyline, slide sorter, and speaker notes. Product management rigor "
                "from Bell Labs produced spec competitors copied for decades."
            ),
        },
        {
            "view": "Cultural backlash didn't kill adoption.",
            "question": "Why does everyone hate PowerPoint but use it?",
            "answer": (
                "Deck culture enables middle-manager communication at scale — "
                "inefficient meetings still beat no structure. Alternatives (Google "
                "Slides) improve collaboration but haven't displaced .pptx in "
                "Fortune 500. Habit plus IT deployment beats UX purity."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "MSFT",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": (
                "PowerPoint exemplifies Office 365 bundle moat — single apps drive "
                "enterprise suite retention; monitor Copilot integration in PowerPoint "
                "as AI upsell vector within productivity segment."
            ),
        }
    ],
    golden_quotes=[
        "\"Microsoft's first acquisition was a Mac app — that tells you everything about Gates' application strategy.\" — David on Forethought deal.",
        "\"Gaskins didn't build slides — he built the presentation job.\" — Ben on category creation.",
        "\"Fourteen million dollars for the way every executive communicates forever.\" — Hosts on ROI.",
    ],
    chronology={
        "subject": "PowerPoint · Forethought · Microsoft",
        "events": [
            {"date": "1984", "event": "Robert Gaskins conceives presentation software at Forethought"},
            {"date": "Apr 1987", "event": "PowerPoint 1.0 ships for Macintosh as 'Presenter' renamed"},
            {"date": "Jul 1987", "event": "Microsoft acquires Forethought for $14M — first acquisition"},
            {"date": "1988", "event": "PowerPoint ports to Windows; joins emerging Office suite"},
            {"date": "1990", "event": "Office bundle launches — Word, Excel, PowerPoint integrated"},
            {"date": "1992", "event": "PowerPoint estimated $100M+ revenue inside Microsoft"},
            {"date": "2000s", "event": ".pptx format standardizes; installed base reaches hundreds of millions"},
            {"date": "2013", "event": "PowerPoint ships real-time co-authoring via Office 365 web apps"},
            {"date": "2015", "event": "Office 365 cloud subscription model replaces boxed Office for most enterprises"},
            {"date": "2018-05-04", "event": "Acquired publishes Forethought/PowerPoint history episode"},
        ],
    },
)

EPISODES["acq-season-2-episode-3nest"] = shell(
    "acq-season-2-episode-3nest",
    meta(
        "acq-season-2-episode-3nest",
        "Nest",
        "Nest",
        "Season 2 · Episode 3",
        "2018-02-19",
        99,
        "https://www.acquired.fm/episodes/season-2-episode-3nest",
    ),
    episode_rating={"overall": 4},
    keywords=["Smart Home", "Tony Fadell", "Google Hardware"],
    conclusion=(
        "Google acquired Nest Labs in January 2014 for $3.2B in cash — betting Tony Fadell's "
        "Apple-honed hardware taste could crack the smart home. Fadell co-invented the iPod at "
        "General Magic alumni network (alongside Android founder Andy Rubin), led 18 generations "
        "of iPod and early iPhone, then retired to build a green thermostat. Nest Learning "
        "Thermostat ($249) sold millions by making ugly HVAC controls desirable; Protect smoke "
        "detectors and Dropcam followed. Integration failed: Nest stayed separate until 2018 "
        "reorg, Fadell departed 2016, and Google merged Nest into Home division. The episode "
        "asks whether $3.2B bought design DNA or merely expensive optionality in a category "
        "Apple and Amazon eventually contested."
    ),
    background=(
        "Ben and David trace Fadell from General Magic (1990) through Philips, Apple iPod/iPhone "
        "leadership, to Nest founding (2010). Nest's direct-to-consumer retail strategy, "
        "machine-learning thermostat behavior, and 2014 Google deal occur amid Larry Page's "
        "hardware ambition and Android@Home failures.\n\n"
        "Post-acquisition culture clash — Nest's premium brand vs Google's ad-driven ethos — "
        "and Revolv shutdown controversy illustrate bigco integration risks. Episode connects "
        "to Amazon Echo (2014), Apple HomeKit, and whether smart home needs one winner or "
        "fragmented standards."
    ),
    important_facts=[
        "Google acquired Nest Labs January 2014 for $3.2B cash; Nest had sold millions of thermostats at $249 retail price point.",
        "Tony Fadell led 18 generations of iPod and co-created iPhone hardware at Apple before founding Nest in 2010.",
        "Nest Learning Thermostat launched 2011; estimated ~11M units sold by 2017 across two generations.",
        "Nest acquired Dropcam for $555M (2014) and Revolv hub company — later bricking Revolv devices in 2016 sparking backlash.",
        "Fadell left Nest June 2016; Google merged Nest into Home hardware division February 2018 under Rick Osterloh.",
    ],
    mental_model={
        "name": "Design-Led Hardware Inside Ad-Driven Software Co",
        "components": (
            "Google excels at software scale and data; hardware needs taste, supply "
            "chain, and brand premium. Fadell brought Apple-like industrial design to "
            "ignored categories (thermostat). $3.2B buys team and brand, not proven "
            "platform — smart home standards fragmented (Thread, Zigbee, Matter later). "
            "Integration fails when ad-company culture meets premium hardware P&L "
            "expectations. Optionality value if home becomes computing battleground; "
            "write-down risk if Echo wins voice hub."
        ),
        "application": (
            "When big tech buys hardware startups, model cultural fit and standalone "
            "brand need. Nest kept separate identity years — signal that Google "
            "couldn't absorb premium positioning. Investors in GOOGL hardware bets "
            "should track Nest/Home revenue disclosure (minimal) versus R&D spend. "
            "Smart home winners may be voice (Alexa) not thermostat UI."
        ),
    },
    competitive_advantage=(
        "Nest's early moat was design plus learning algorithm — thermostat that "
        "programs itself from behavior, sold through Apple Stores and premium retail. "
        "Fadell's Apple supply-chain relationships and marketing craft created "
        "category respect competitors (Honeywell) lacked.\n\n"
        "Google added data center ML, voice assistant integration path, and cross-subsidy "
        "from search profits. Dropcam extended into security cameras — recurring "
        "services potential.\n\n"
        "Weaknesses: Amazon Echo (2014) captured voice hub; Revolv shutdown eroded trust; "
        "Fadell departure lost founder drive; premium pricing limited mass adoption "
        "versus sub-$50 Alexa dots. Google eventually unified under Home brand, diluting "
        "Nest premium.\n\n"
        "Versus Apple HomeKit (slow) or Amazon (voice-first), Nest bet on beautiful "
        "devices — partial win in thermostats, lost hub war."
    ),
    key_insights=[
        {
            "view": "$3.2B bought Apple hardware DNA, not smart home victory.",
            "question": "Why pay billions for thermostats?",
            "answer": (
                "Google feared missing next platform after mobile — home sensors "
                "generate data and lock-in. Fadell's team proved hardware taste; "
                "~11M thermostats validated product-market fit at premium tier. Larry "
                "Page's bet: Nest becomes home OS before Amazon or Apple seal category."
            ),
        },
        {
            "view": "General Magic alumni shaped two mobile eras.",
            "question": "What's the Andy Rubin connection?",
            "answer": (
                "Fadell and Rubin both passed through General Magic (1990) — failed "
                "PDA pioneer that trained a generation (Pierre Omidyar too). Rubin "
                "built Android; Fadell built iPod then Nest. Episode uses lineage to "
                "show smart home as sequel to smartphone platform wars."
            ),
        },
        {
            "view": "Revolv shutdown was trust catastrophe.",
            "question": "What integration mistake hurt Nest?",
            "answer": (
                "Google bricking Revolv hubs in 2016 — acquired 2014 — told buyers "
                "Google could kill hardware support. Premium hardware requires longevity "
                "promises antithetical to Google's product-kill culture. Amazon exploited "
                "with Echo reliability narrative."
            ),
        },
        {
            "view": "Voice beat touch for home hub.",
            "question": "Did Nest lose to Echo?",
            "answer": (
                "Nest thermostat succeeded in niche; Echo (mid-2014) became command "
                "center for lights, music, shopping. Voice interaction beat walking "
                "to wall thermostat. Google eventually prioritized Assistant speakers "
                "over Nest hub identity — strategic pivot Fadell resisted."
            ),
        },
        {
            "view": "Founder exit signaled integration failure.",
            "question": "Why did Fadell leave 2016?",
            "answer": (
                "Culture clash with Google leadership, Dropcam integration stress, "
                "and Alphabet reorg friction. Hardware founders rarely survive "
                "ad-company bureaucracy — parallel to Meta's Oculus struggles. "
                "2018 Nest-Home merge formalized loss of independent brand strategy."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "GOOGL",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": (
                "Nest $3.2B bet remains immaterial to Google P&L but illustrates "
                "hardware integration difficulty — monitor Google Home/Matter strategy "
                "versus Amazon smart home attach rates."
            ),
        },
        {
            "ticker": "AMZN",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": (
                "Echo voice-hub victory over Nest thermostat-first strategy supports "
                "Amazon smart home commerce flywheel — Ring/Alexa ecosystem benefits "
                "from Google's Nest fragmentation."
            ),
        },
    ],
    golden_quotes=[
        "\"Tony Fadell made thermostats sexy — that's not a sentence anyone said before 2011.\" — Hosts on design-led category creation.",
        "\"Three point two billion for the iPod guy's retirement project.\" — David on deal headline.",
        "\"Google bricked Revolv — and bricking trust is harder to fix.\" — Ben on integration misstep.",
    ],
    chronology={
        "subject": "Nest · Google · Tony Fadell",
        "events": [
            {"date": "1990", "event": "General Magic founded; Fadell and Andy Rubin among alumni"},
            {"date": "2001", "event": "Tony Fadell joins Apple; leads iPod development"},
            {"date": "2007", "event": "Fadell co-leads iPhone hardware program"},
            {"date": "2010", "event": "Fadell founds Nest Labs after leaving Apple"},
            {"date": "2011", "event": "Nest Learning Thermostat launches at $249 retail"},
            {"date": "Jan 2014", "event": "Google acquires Nest for $3.2B cash"},
            {"date": "2014", "event": "Nest buys Dropcam for $555M; Amazon launches Echo"},
            {"date": "2016", "event": "Google bricks Revolv hubs; Fadell departs Nest"},
            {"date": "Feb 2018", "event": "Google merges Nest into Home hardware division"},
            {"date": "2018-02-19", "event": "Acquired publishes Nest acquisition episode"},
        ],
    },
)

EPISODES["acq-arm-softbank"] = shell(
    "acq-arm-softbank",
    meta(
        "acq-arm-softbank",
        "ARM & SoftBank",
        "ARM & SoftBank",
        "Season 4 · Episode 2",
        "2019-02-03",
        89,
        "https://www.acquired.fm/episodes/arm-softbank",
    ),
    episode_rating={"overall": 5},
    keywords=["ARM Architecture", "SoftBank Vision Fund", "Fabless Semiconductors"],
    conclusion=(
        "ARM began as Acorn Computers' 1983 RISC side project in Cambridge, England — spun out "
        "1990 with Apple and VLSI as investors to build processors for the Newton. Apple nearly "
        "died; ARM pivoted to licensing IP rather than selling chips, powering Nokia phones then "
        "95%+ of smartphones. SoftBank acquired ARM in July 2016 for $32B (~43% premium) — "
        "Masayoshi Son's bet that IoT would need trillions of connected chips. ARM's royalty "
        "model (~$2B revenue pre-deal, ~95% gross margins) became blueprint for Vision Fund "
        "thesis: own infrastructure of next computing wave. Nvidia's failed $40B ARM buy (2022) "
        "and 2023 IPO at ~$54B market cap validate Son's pricing. From Isaac Newton's college town "
        "to every pocket on Earth — architecture beats fabrication when mobile wins."
    ),
    background=(
        "Ben and David trace ARM from Acorn BBC Micro (1981) through Sophie Wilson and Steve "
        "Furber's RISC chip (1985), Apple Newton alliance, and licensing model that made ARM "
        "neutral Switzerland of semiconductors. Contrasts Intel's IDM vertical integration vs "
        "ARM's fabless IP royalties on every Qualcomm, Apple, and Samsung chip.\n\n"
        "SoftBank's 2016 takeover, Son's 300-year Vision Fund ambition, and ARM's role in "
        "iPhone/Android standardization frame the episode. Meetup promo for 1M downloads ties "
        "to Acquired community growth parallel to ARM's invisible ubiquity."
    ),
    important_facts=[
        "SoftBank acquired ARM Holdings in July 2016 for $32B cash — 43% premium to pre-announcement trading price.",
        "ARM founded 1990 spinout from Acorn Computers; licensing model generates ~$2B annual revenue at ~95% gross margins pre-acquisition.",
        "ARM processor designs power estimated 95%+ of smartphone application processors and 125B+ chips shipped cumulative by late 2010s.",
        "Apple invested in 1990 ARM spinout for Newton; ARM stake later helped Apple survive 1990s — sold stake for ~$800M gain.",
        "ARM returned to public markets September 2023 IPO at ~$54B valuation after Nvidia's $40B acquisition attempt failed regulatory review (2022).",
    ],
    mental_model={
        "name": "Architecture Licensing Beats Fabrication in Mobile",
        "components": (
            "Intel won PC era owning fabs + x86. Mobile needed power efficiency — "
            "ARM's RISC designs licensed to every chipmaker without competing with "
            "customers. Royalty per chip scales with volume; capex near zero vs "
            "Intel's $20B+ fabs. Neutral IP vendor avoids Samsung-vs-Apple conflict. "
            "SoftBank paid $32B for toll booth on IoT + mobile compute — Vision Fund "
            "thesis applied to one asset. Risk: RISC-V open architecture and customer "
            "vertical integration (Apple M-series)."
        ),
        "application": (
            "In semis, identify layers capturing rent without capital intensity. ARM "
            "analogous to TSMC (manufacturing) or Synopsys (EDA) — pick non-conflicted "
            "chokepoint. Masa Son's $32B bet priced optionality on 1T connected devices; "
            "2023 IPO proved market agreed. Investors compare ARM royalty growth vs "
            "RISC-V disruption timeline."
        ),
    },
    competitive_advantage=(
        "ARM's moat is instruction-set ecosystem — decades of software, tools, and "
        "engineer training on ARM assembly. Switching to RISC-V or x86 requires "
        "recompilation, revalidation, and OS support. Apple, Qualcomm, Amazon Graviton "
        "all license ARM — no single customer can kill standard.\n\n"
        "Licensing model scales: ARM designs cores (Cortex-A, M, R); partners add "
        "modems, GPUs, custom blocks. ~95% gross margin because ARM never fabs — "
        "TSMC bears capex.\n\n"
        "Weaknesses: per-chip royalties cap upside on $10 ASP IoT parts; Apple "
        "Architectural License reduces royalty rate on M-series; RISC-V gains in "
        "embedded; China geopolitics threaten licensing revenue. SoftBank leverage "
        "post-acquisition added debt burden until IPO recap.\n\n"
        "Versus Intel mobile failures (Atom) or MIPS, ARM won neutral licensing plus "
        "mobile timing — Cambridge RISC heritage became industry default."
    ),
    key_insights=[
        {
            "view": "Licensing model was accident then strategy.",
            "question": "Why doesn't ARM make chips?",
            "answer": (
                "1990 spinout lacked fab capital; Apple wanted IP not competitor. "
                "Licensing to Nokia, Qualcomm, Samsung simultaneously built ecosystem "
                "Intel couldn't replicate — IDM model forbade serving all mobile "
                "rivals. Neutrality became moat; ~95% gross margins prove capital-light "
                "scale."
            ),
        },
        {
            "view": "Apple's ARM stake saved both companies.",
            "question": "How did ARM help Apple survive?",
            "answer": (
                "Apple invested in 1990 ARM spinout; later sold ARM shares for ~$800M "
                "during 1990s distress — liquidity when Apple neared bankruptcy. Irony: "
                "ARM in every iPhone today traces to Newton-era alliance. Strategic "
                "investments in suppliers can return when core business falters."
            ),
        },
        {
            "view": "SoftBank bought IoT optionality at $32B.",
            "question": "Why did Masa Son pay 43% premium?",
            "answer": (
                "Son projected 1T IoT devices needing ARM cores — licensing toll on "
                "trillions of chips justifies premium over ~$2B revenue. Vision Fund "
                "launched same era; ARM deal was thesis statement. 2023 ~$54B IPO "
                "validated price despite Nvidia block."
            ),
        },
        {
            "view": "Intel lost mobile before ARM won.",
            "question": "How did Cambridge dethrone Intel?",
            "answer": (
                "x86 power draw unsuitable for phones; Intel Atom failed carrier "
                "design wins. ARM licensed to every Android OEM via Qualcomm/MediaTek. "
                "By 2010s 95%+ smartphone APs ARM-based — Intel missed entire mobile "
                "compute wave while dominating data center."
            ),
        },
        {
            "view": "RISC-V is credible long-term threat.",
            "question": "Can open source displace ARM?",
            "answer": (
                "RISC-V offers royalty-free ISA for embedded/China geopolitical needs. "
                "ARM's software ecosystem and architectural licenses delay transition "
                "years. Episode notes ARM must keep royalty rates low enough to prevent "
                "collective customer defection — same antitrust logic Qualcomm faces."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "ARM",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": (
                "Post-2023 IPO, ARM trades as pure-play ISA toll booth — monitor "
                "royalty growth from AI edge chips and Apple/Qualcomm architectural "
                "license mix versus RISC-V adoption in China."
            ),
        },
        {
            "ticker": "SFTBY",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": (
                "ARM IPO recap reduced SoftBank leverage; 2016 $32B bet returned capital "
                "plus validated Son's infrastructure thesis — remaining Vision Fund "
                "assets still carry WeWork-era scar tissue."
            ),
        },
    ],
    golden_quotes=[
        "\"ARM doesn't make chips — it taxes every chip everyone else makes.\" — Hosts on licensing model.",
        "\"Apple sold ARM stock to survive the 90s; now they pay ARM royalties on every iPhone.\" — David on strategic circle.",
        "\"Thirty-two billion for the blueprint of the Vision Fund.\" — Ben on SoftBank acquisition logic.",
    ],
    chronology={
        "subject": "ARM · SoftBank · Mobile Computing",
        "events": [
            {"date": "1981", "event": "Acorn Computers wins BBC Micro contract; establishes Cambridge base"},
            {"date": "1985", "event": "Sophie Wilson and Steve Furber design Acorn RISC Machine (ARM)"},
            {"date": "1990", "event": "ARM Ltd spun out with Apple and VLSI investment for Newton"},
            {"date": "1993", "event": "Apple Newton launches with ARM processor — commercial failure"},
            {"date": "1998", "event": "ARM IPO on LSE and NASDAQ; Nokia mobile licensing accelerates"},
            {"date": "2007", "event": "iPhone launches — ARM architecture in every smartphone generation"},
            {"date": "Jul 2016", "event": "SoftBank acquires ARM for $32B — 43% premium"},
            {"date": "2017", "event": "SoftBank Vision Fund launches $100B — ARM as thesis anchor"},
            {"date": "2020", "event": "Nvidia announces $40B ARM acquisition attempt"},
            {"date": "2022", "event": "Nvidia-ARM deal terminated amid regulatory opposition"},
            {"date": "Sep 2023", "event": "ARM IPO at ~$54B valuation on NASDAQ"},
        ],
    },
)

EPISODES["acq-season-4-episode-1-espn"] = shell(
    "acq-season-4-episode-1-espn",
    meta(
        "acq-season-4-episode-1-espn",
        "ESPN",
        "ESPN",
        "Season 4 · Episode 1",
        "2019-01-20",
        89,
        "https://www.acquired.fm/episodes/season-4-episode-1-espn",
    ),
    episode_rating={"overall": 5},
    keywords=["Sports Media", "Cable Bundling", "Live Rights"],
    conclusion=(
        "ESPN began in 1979 when failed TV weatherman Bill Rasmussen rented satellite transponder "
        "time and built studios on a Bristol, Connecticut landfill — America's first 24-hour sports "
        "network. Getty Oil funded early losses; ABC bought 15% then full control; Disney acquired "
        "Cap Cities/ABC in 1996 for $19B, inheriting ESPN. Live sports rights — NFL Monday Night "
        "Football (1987, $153M/year era deals), NBA, MLB — created must-have cable bundle anchor "
        "generating ~$8B+ revenue and ~$4B+ operating profit at peak. ESPN+ streaming (2018, $4.99/mo) "
        "responds to cord-cutting but risks cannibalizing ~$9/month affiliate fees from 90M+ "
        "households. The episode: live sports is the last moat of linear TV — until leagues "
        "direct-to-consumer."
    ),
    background=(
        "Season 4 opens with ESPN's improbable origin — Rasmussen brothers, Connecticut Whalers "
        "hockey tape delays, and satellite economics enabling national niche network. Ben and David "
        "walk through SportsCenter invention, Chris Berman era, John Skipper leadership, and "
        "$15B+ annual sports rights inflation.\n\n"
        "They analyze cable bundle mechanics: ESPN charges distributors ~$9/subscriber/month — "
        "highest affiliate fee — because operators fear churn without live games. Streaming "
        "pivot, Disney+ bundle strategy, and league-owned DTC (NFL+, NBA League Pass) threaten "
        " decades-long model."
    ),
    important_facts=[
        "ESPN launched September 7, 1979 as first 24-hour sports cable network; initial reach ~1.4M households.",
        "Getty Oil invested ~$154M cumulative before profitability; ABC acquired full ESPN control by 1984.",
        "Disney acquired Cap Cities/ABC (including ESPN) in 1996 for $19B — ESPN became profit engine worth multiples of deal price.",
        "ESPN peak operating income exceeded $4B (mid-2010s); revenue ~$8B+ with affiliate fees ~$9/month from ~90M subscribing households.",
        "ESPN+ streaming service launched April 2018 at $4.99/month; 24M+ subscribers by 2023 but fraction of linear affiliate economics.",
    ],
    mental_model={
        "name": "Live Rights as Cable Bundle Anchor",
        "components": (
            "Sports are DVR-proof — live games force simultaneous viewing, making "
            "advertising and affiliate fees valuable. ESPN aggregates rights across "
            "leagues, charging cable operators ~$9/sub highest in bundle — operators "
            "pay because sports fans churn without ESPN. Flywheel: rights payments → "
            "better games → higher affiliate fees → bid more for rights. Streaming "
            "breaks bundle: DTC caps household reach vs linear mandatory carriage. "
            "Leagues eventually bypass network middlemen (NBA/WNBA deals evolving)."
        ),
        "application": (
            "Media investors must model affiliate fee decline versus streaming ARPU. "
            "ESPN's ~$9×90M households dwarfs ESPN+ $5×24M subs — cord-cutting is "
            "existential even if streaming grows. Live rights inflation ($15B+ industry "
            "wide) squeezes network margins — Disney must balance ESPN P&L with "
            "Disney+ subscriber growth strategy."
        ),
    },
    competitive_advantage=(
        "ESPN's moat was first-mover 24-hour sports brand plus long-term exclusive "
        "rights — SportsCenter culture, NFL Monday Night Football (1987), and "
        "multi-sport breadth competitors couldn't match. Cable bundle forced every "
        "household to subsidize sports fans — widest tax base in media.\n\n"
        "Disney ownership added Marvel/Star Wars cross-promotion, theme park tie-ins, "
        "and balance sheet for rights bidding wars versus Fox Sports or Turner.\n\n"
        "Weaknesses: cord-cutting removes forced subsidy; leagues launch direct streams; "
        "rights costs up ~10× since 1990s; younger audiences on highlights (YouTube, "
        "TikTok) not linear. ESPN+ priced low to avoid cannibalization — trapped "
        "between legacy cash cow and streaming future.\n\n"
        "Versus regional sports networks (RSN collapse) or NBC Sports, ESPN survived "
        "longest on national rights portfolio — but NFL Sunday Ticket to YouTube "
        "(2023, ~$2B/year) signals league power shift."
    ),
    key_insights=[
        {
            "view": "Landfill origin story masks sophisticated economics.",
            "question": "How did a weatherman build ESPN?",
            "answer": (
                "Rasmussen exploited satellite transponder lease — national reach "
                "before regional sports networks. Connecticut location near NYC "
                "talent; Getty Oil capital survived years of losses. First-mover in "
                "24-hour niche created brand before competitors — classic cable era "
                "distribution arbitrage."
            ),
        },
        {
            "view": "Affiliate fees beat advertising.",
            "question": "Where does ESPN's profit come from?",
            "answer": (
                "~$9/month × ~90M households ≈ $9B+ affiliate revenue at peak — "
                "advertising secondary. Cable operators pay because sports fans "
                "cancel bundles without ESPN. Forced bundle subsidy is moat; "
                "streaming unbundles the tax base."
            ),
        },
        {
            "view": "Rights inflation is prisoner’s dilemma.",
            "question": "Why do sports rights keep rising?",
            "answer": (
                "Leagues auction exclusivity; networks bid defensively to prevent "
                "rival carriage. NFL Monday Night Football deals grew from ~$153M "
                "(1987 era) toward billions annually industry-wide. Winners pay more "
                "than rational ROI — ESPN must bid to protect affiliate fee leverage."
            ),
        },
        {
            "view": "ESPN+ is hedge, not replacement.",
            "question": "Why launch streaming at $4.99?",
            "answer": (
                "Price below affiliate economics intentionally — Disney feared "
                "cannibalizing ~$9 cable fee. 24M ESPN+ subs by 2023 generate far "
                "less than lost linear households. Strategic optionality until leagues "
                "force full DTC migration."
            ),
        },
        {
            "view": "Leagues are becoming competitors.",
            "question": "What ends ESPN's moat?",
            "answer": (
                "NFL Sunday Ticket to YouTube (~$2B/year, 2023), NBA media deals "
                "fragmenting, league-owned apps bypass networks. ESPN becomes bidder "
                "for rights it once monopolized — margin compression inevitable as "
                "Disney pivots to Disney+ general entertainment."
            ),
        },
    ],
    top_investment_implications=[
        {
            "ticker": "DIS",
            "direction": "Watch",
            "confidence": "Medium",
            "thesis": (
                "ESPN remains Disney cash cow but cord-cutting compresses affiliate "
                "fees — monitor ESPN+ DTC pivot and sports rights renewal economics "
                "versus linear subscriber decline rate."
            ),
        },
        {
            "ticker": "GOOGL",
            "direction": "Watch",
            "confidence": "Low",
            "thesis": (
                "YouTube's NFL Sunday Ticket deal (~$2B/year) signals tech platforms "
                "bypassing ESPN for live sports — watch for further league DTC "
                "partnerships eroding traditional network moats."
            ),
        },
    ],
    golden_quotes=[
        "\"They built the worldwide leader in sports on a literal dump in Bristol, Connecticut.\" — David on Rasmussen origin.",
        "\"Nine dollars a month from ninety million homes — that's the moat.\" — Ben on affiliate fee economics.",
        "\"Live sports is the last thing America watches together — and the leagues know it.\" — Hosts on rights inflation.",
    ],
    chronology={
        "subject": "ESPN · Cable Sports Media",
        "events": [
            {"date": "Sep 1979", "event": "ESPN launches as first 24-hour sports cable network from Bristol, CT"},
            {"date": "1979–83", "event": "Getty Oil invests ~$154M; network reaches ~1.4M households"},
            {"date": "1984", "event": "ABC acquires full control of ESPN"},
            {"date": "1987", "event": "ESPN wins NFL Monday Night Football — landmark live rights deal"},
            {"date": "1996", "event": "Disney acquires Cap Cities/ABC for $19B, including ESPN"},
            {"date": "2006", "event": "ESPN launches ESPN360 streaming precursor to modern DTC"},
            {"date": "Mid-2010s", "event": "ESPN peak — ~$4B+ operating income, ~90M subscribing households"},
            {"date": "Apr 2018", "event": "ESPN+ launches at $4.99/month as cord-cutting accelerates"},
            {"date": "2023", "event": "NFL Sunday Ticket moves to YouTube (~$2B/year) — league DTC shift"},
            {"date": "2019-01-20", "event": "Acquired Season 4 opens with ESPN history episode"},
        ],
    },
)
