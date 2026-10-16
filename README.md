# Free remote MCP servers (tested weekly)

Remote [Model Context Protocol](https://modelcontextprotocol.io) servers from the [official MCP Registry](https://registry.modelcontextprotocol.io) that answer **without any API key, token or login**. Every server is re-tested each week with exactly two requests, `initialize` and `tools/list`. No tool is ever called.

**Last run: 2026-10-16** · 17,070 endpoints tested · **9,620 open (56 %)** · 5,166 need auth · 2,284 not working · 7,690 listed after removing copies

- Full list: [`data/servers.csv`](data/servers.csv) and [`data/servers.json`](data/servers.json)
- Browse with search and topics: [shortformkit.com/free-remote-mcp-servers](https://shortformkit.com/free-remote-mcp-servers/)
- Check any server yourself: [MCP Server Tester](https://shortformkit.com/mcp-server-tester/)

## Add a server to your client

| Client | How |
|---|---|
| Claude (claude.ai, desktop) | Settings, Connectors, Add custom connector, paste the URL |
| Claude Code | `claude mcp add --transport http NAME URL` |
| Cursor | `{"mcpServers": {"NAME": {"url": "URL"}}}` in `~/.cursor/mcp.json` |
| VS Code | `{"servers": {"NAME": {"type": "http", "url": "URL"}}}` in `.vscode/mcp.json` |

## Picks by topic

Up to 25 per topic: one per publisher, 3 to 40 tools, servers with a website or repo first, fastest first. Open means usable without signing up, not an endorsement: read what a server does before you connect it.


### Search and web

| Server | What it does | URL | Tools |
|---|---|---|---|
| [HotelsCasa](https://hotelscasa.com/) | Travel search: 1.3M hotels and apartments, owner homes, tours, flights, taxi, car rental. | `https://mcp.hotelscasa.com/mcp` | 13 |
| [mcp](https://karusele.com) | Search Karusele stainless steel products and get product details via AI agents. | `https://mcp.karusele.com/mcp` | 5 |
| [TheAIMeters](https://www.theaimeters.com/) | Read-only AI impact metrics with search, methodology and cited sources. No authentication required. | `https://www.theaimeters.com/mcp` | 5 |
| [Immobilien Eichmann – Angebote](https://immobilieneichmann.de/) | Live MCP for Immobilien Eichmann listings (Konstanz). Tools: search_listings, get_listing. | `https://immobilieneichmann.de/mcp` | 4 |
| [DiscGolfAPI MCP](https://discgolfapi.com) | Search disc golf courses worldwide, find nearby courses, and retrieve course details and updates. | `https://io.discgolfapi.com/mcp` | 4 |
| [OmniForce](https://github.com/rmb/omniforce-mcp) | AI-search visibility: GEO audits, tracked prompts, competitors, citations. | `https://mcp-oss.omniforce.run/mcp` | 8 |
| [Public Board — Anonymous Message Board for AI Agents](https://public-board.com) | Message board for AI agents: read, search and leave notes over HTTP, DNS or a non-CDN mirror. | `https://public-board.com/mcp` | 3 |
| [ScrubShifts Healthcare Jobs](https://scrubshifts.com) | Live US nursing and allied-health jobs, updated daily. Search by place, role, shift, pay. | `https://scrubshifts.com/mcp` | 4 |
| [New Runtime public records](https://newruntime.com/agents/) | AI-engineering archive: search, what is new, forecasts, topic briefs, URL context; moderated inbox. | `https://newruntime.com/mcp` | 14 |
| [GTH Intelligence - Substance Abuse Treatment Finder](https://github.com/Crindo2/gth-mcp-server) | Search 12,338 curated, SAMHSA-sourced addiction treatment facilities across all 50 US states. | `https://gth-mcp-server.pages.dev/mcp` | 4 |
| [IA-Asso.fr — French Associations Registry](https://ia-asso.fr) | Search 1.26M+ active French associations (official RNA registry, 10 tools, premium & RUP filters) | `https://ia-asso.fr/api/mcp` | 18 |
| [DealerMax](https://dealermax.app) | Italian cross-dealer MCP: cars, NLT rentals with quotations, dealer directory, automotive KB. | `https://mcp.dealermax.app/mcp/` | 7 |
| [SigmaDiario — Datos de Argentina](https://sigmadiario.com/desarrolladores) | Live Argentina data: dolar rates, quiniela and lotteries, holidays, river levels, inflation, news. | `https://sigmadiario.com/api/mcp` | 7 |
| [server](https://github.com/jhibird/HeySpark-MCP) | Search and discover local businesses. 30+ categories with verified contact info, hours, and reviews. | `https://mcp.heyspark.co/mcp` | 4 |
| [aicoolies](https://aicoolies.com) | Search and read the aicoolies catalog of AI and developer tools via a remote MCP knowledge graph. | `https://aicoolies.com/mcp` | 11 |
| [NeoDemos](https://neodemos.nl) | Source-anchored search and civic intelligence for Dutch municipal council records. | `https://mcp.neodemos.nl/public/mcp` | 7 |
| [Youth4work (public, no sign-in)](https://mcp.youth4work.com/) | Read-only search of Youth4work public jobs, assessed talent, exam mock tests and Indian colleges. | `https://mcp.youth4work.com/public/mcp` | 9 |
| [Bro Find AI](https://brofindai.com/brofindai-mcp) | Search a curated directory of AI tools, AI agents and MCP servers by task, pricing and platform. | `https://brofindai.com/api/mcp` | 5 |
| [Sail](https://sailrides.co/about/integrate) | Search places, compare ride-hailing options, and plan trotro minibus journeys. | `https://sailrides.co/mcp` | 6 |
| [Ace Website MCP](https://ace-bl.tech/connect) | Search and read public Ace pages with source URLs. | `https://ace-bl.tech/mcp` | 6 |
| [workorai](https://github.com/work0r-ai/agent-kit) | WorkorAI talent marketplace MCP: candidate job search and employer hiring with explainable matching | `https://workorai.com/mcp` | 29 |
| [pixdress — KI-Mode zum Selbermachen](https://pixdress.de/llms.txt) | Search AI-designed print-on-demand clothing, or have a new motif invented from one sentence. | `https://pixdress.de/mcp` | 3 |
| [fysio.care clinic discovery](https://fysio.care/developers) | Discover Swedish MSK clinics on fysio.care: search clinics, services, and open appointment times. | `https://fysio.care/api/mcp` | 4 |
| [World Resolver](https://github.com/ajithisaac/world-resolver-mcp) | Resolve real-world capability gaps: validate native MCPs, search the web, and record unmet demand. | `https://world-resolver-mcp.ajithisaac.workers.dev/mcp` | 9 |
| [msza.ai — Polish Catholic Sermons ✝](https://msza.ai) | Search public Polish Catholic sermons, transcripts, Scripture, prayers, churches and daily content. | `https://msza.ai/mcp` | 17 |

### Documentation and knowledge

| Server | What it does | URL | Tools |
|---|---|---|---|
| [nyuchi-docs](https://docs.nyuchi.com/integrations/docs-mcp/) | Search, read, and ask the Nyuchi docs (docs.nyuchi.com); send feedback or raise issues. | `https://docs.nyuchi.com/mcp` | 5 |
| [Helsama](https://helsama.se) | Hemp from Gotland: product catalog, knowledge base and open lab data per batch. | `https://helsama.se/mcp` | 6 |
| [UseMyContext.ai](https://usemycontext.ai) | Personal context for AI, written by you and never scraped: your profile and files, any MCP client. | `https://mcp.usemycontext.ai/mcp` | 13 |
| [Nasaq UI](https://nasaqui.com) | Nasaq design system docs for agents: 390 components for React, Vue, Blade and HTML, with Arabic RTL. | `https://mcp.nasaqui.com/mcp` | 6 |
| [New Mexico Literacy Project](https://newmexicoliteracyproject.org) | Free book-donation pickup logistics and first-edition identification tools for New Mexico. | `https://newmexicoliteracyproject.org/api/mcp` | 16 |
| [GROO reality](https://www.groo.cz/pro-ai) | Nabídka nemovitostí GROO reality — byty, domy a pozemky v Praze a okolí. Jen pro čtení, bez klíče. | `https://www.groo.cz/mcp` | 12 |
| [Ghosty Studio docs](https://www.ghosty.studio/docs) | Docs de Ghosty Studio para agentes: búsqueda, páginas en markdown, índice y OpenAPI. Sin auth. | `https://www.ghosty.studio/mcp/docs` | 4 |
| [ClearMarket](https://clearmarket.fyi) | Reference data for prediction markets: graded resolution clarity, cross-venue links, provenance. | `https://api.clearmarket.fyi/mcp` | 6 |
| [AskSakina Islamic Knowledge](https://www.asksakina.com) | Curated Islamic MCP: Quran (Arabic + Pickthall), 440 du'as, 99 Names, crisis-aware. | `https://sakina-mcp.fly.dev/mcp` | 4 |
| [AI 與科技名詞白話解釋](https://tw-ai-glossary.panda198271.workers.dev) | AI 與科技名詞白話解釋、概念比較與入門教學（繁體中文）。 | `https://tw-ai-glossary.panda198271.workers.dev/mcp` | 6 |
| [CalvingWatch Public Knowledge](https://calvingwatch.com/ai/) | Read-only CalvingWatch product, tester, camera, privacy and safety facts; no customer data. | `https://calvingwatch.com/mcp` | 5 |
| [Electrik Slate](https://slate.electrik.dev/docs/ai) | Read-only MCP for Electrik Slate: Blade component docs, blocks gallery, source, and llms.txt. | `https://mcp.slate.electrik.dev` | 6 |
| [Lithuanian Data Portal documentation](https://guides.dataportal.gov.lt/docs/mcp) | Search and read the Lithuanian Data Portal user guide and Data API docs, in Lithuanian and English | `https://guides.dataportal.gov.lt/api/mcp` | 3 |
| [NVIDIA NemoClaw CKG](https://github.com/Yarmoluk/ckg-nvidia-nemoclaw) | NVIDIA NemoClaw knowledge graph — 55 nodes, F1 0.576 (+269% vs RAG), 11x fewer tokens. MCP-native. | `https://ckg-nvidia-nemoclaw.onrender.com/mcp` | 8 |
| [docs](https://freebatteryfactory.com) | Search and read the Free Battery Factory docs (LiteShip, batpak) as live MCP tools. | `https://freebatteryfactory.com/mcp` | 5 |
| [Agents Wiki](https://agents-wiki.com/connect) | Knowledge base for AI agents: search, read, tasks; write, correct, report outcomes via /mcp/write. | `https://agents-wiki.com/mcp` | 6 |
| [web3ctx](https://web3ctx.scarai.xyz) | Version-true web3 docs, ABIs and human-validated integration recipes over MCP. | `https://mcp.scarai.xyz/mcp` | 5 |
| [Grok Bot Wiki](https://www.grokbotwiki.com/mcp) | Read-only search of community Grok Bot templates and guides. Unofficial; not affiliated with xAI. | `https://www.grokbotwiki.com/api/mcp` | 8 |
| [Traffic Parrot](https://trafficparrot.com/ai/agent-trial.html) | Traffic Parrot simulates APIs and messaging. Request or withdraw a trial, read docs, send feedback. | `https://mcp.trafficparrot.com/` | 6 |
| [reference](https://cuttingtoolsai.eu) | Brand-neutral cutting tool reference: grade cross-reference, materials, turning starting values. | `https://cuttingtoolsai.eu/mcp` | 3 |
| [agent-manager.dev documentation](https://agent-manager.dev) | Docs for agent-manager, the terminal UI that runs AI coding agents as live tmux sessions. | `https://agent-manager.dev/mcp` | 6 |
| [Hermes — Air Quality Intelligence](https://www.southlondonscientific.com) | UK air quality MCP: live readings, historical trends, LAQM stats, WHO checks, knowledge base. | `https://hermes.southlondonscientific.com/mcp` | 15 |
| [hibot](https://hibot.com) | HiBot public knowledge: the ANSWER framework for AI visibility, audit plans, case studies, research | `https://hibot.com/mcp/public` | 5 |
| [Captia Industrial Knowledge](https://www.captiatechnology.com/en/mcp/) | Industrial glossary, protocol reference, technical search and OEE calculation. Read-only. | `https://www.captiatechnology.com/api/mcp/` | 6 |
| [Docsy](https://docsy.remcp.site) | Read versioned developer documentation with original source links using five public MCP tools. | `https://docsy.remcp.site/mcp` | 5 |

### Developer tools

| Server | What it does | URL | Tools |
|---|---|---|---|
| [FabTally Decode](https://decode.fabtally.com) | Decode EVM bytes to JSON: event-log decoder, calldata explainer, selector lookup, ABI fetch. | `https://decode.fabtally.com/mcp` | 4 |
| [US Tariff Lookup](https://github.com/profitpather/profitpather-tools) | Find the right US tariff code for a product and the duty rate that actually governs it. | `https://tools.profitpather.com/duty/mcp` | 3 |
| [Desvela ARD Registry — free preflight(domain)](https://desvela.ai/census/) | What a domain publishes for AI agents: ai-catalog.json, llms.txt, agents.md, robots.txt rules. Free. | `https://registry.desvela.dev/mcp` | 4 |
| [Forest Factory](https://forestfactory.dev/) | Paid x402 agent: API discovery,commerce availability/buyable,domain/package preflight,release asset | `https://http--forest-gas-station-mainnet--lcjl27p8lmjs.code.run/mcp` | 10 |
| [MoltNode by Chord](https://moltnode.ag/agents) | Read 31 blockchains over JSON-RPC and swap via Chord: best route, unsigned tx, simulation. No key. | `https://moltnode.ag/mcp` | 7 |
| [EOSL.ai — Hardware End-of-Life Database](https://eosl.ai/mcp/) | Hardware end-of-life dates by part number, each linked to the vendor's own bulletin. | `https://eosl.ai/mcp` | 5 |
| [US Economic, SEC EDGAR & On-Chain Data (x402)](https://github.com/ktcod/x402-json-repair-mcp) | 21 paid tools: US macro data, SEC EDGAR filings, on-chain EVM reads. Settled in USDC on Base. | `https://x402.agentfund.net/mcp` | 21 |
| [GenHTTP Lambda](https://genhttp.dev) | Write, deploy and host small C# web services and sites at a public address. | `https://genhttp.dev/mcp` | 25 |
| [Website Starter](https://websitestarter.org/en/mcp/) | Create Markdown instructions for AI agents to build, deploy, and maintain an Astro website. | `https://websitestarter.org/mcp` | 4 |
| [rows.page](https://rows.page) | Push CSV, JSON, JSONL or Parquet from your agent and get a link a human can explore. | `https://rows.page/mcp` | 6 |
| [cv.json — open CV data](https://cvjson.com) | Search people open to work and fetch their machine-readable cv.json, from any AI assistant. | `https://freecv.org/api/mcp` | 4 |
| [UNE Sino-Gateway](https://legal.une.education/sino) | PRC Civil Code & CISG legal computation engine for Sino-Occidental trade dispute settlement. | `https://legal.une.education/sino/mcp.php` | 4 |
| [Fast GST Refund](https://fastgstrefund.com/for-agents/) | Prepare Indian GST refund records, validate entries and generate Statement 3 and Annexure B JSON. | `https://fastgstrefund.com/mcp` | 11 |
| [SzuruSzuru – rezerwacja czyszczenia tapicerki](https://szuruszuru.pl/llms.txt) | Quote, check slots and book on-site upholstery, carpet and mattress cleaning in Pomorskie, Poland. | `https://agent.szuruszuru.pl/mcp` | 13 |
| [Max Eats Out](https://www.maxeatsout.club/developers) | Editorial guide to restaurants and bars — hand-picked venues with opinions, not a places database | `https://www.maxeatsout.club/api/mcp` | 4 |
| [Feedback Synthesis MCP](https://github.com/sapph1re/feedback-synthesis-mcp) | Synthesize GitHub Issues, HN and App Store reviews into ranked pain clusters. Pay-per-call x402. | `https://feedback-synthesis-mcp-production.up.railway.app/mcp` | 4 |
| [FreshContext](https://freshcontext.dev) | Context integrity for AI agents: evaluate freshness, confidence, provenance, and decision readiness. | `https://api.freshcontext.dev/mcp` | 22 |
| [API Status Check](https://apistatuscheck.com) | Live status probes plus published uptime and incident history for 280+ APIs and cloud services. | `https://apistatuscheck.com/api/mcp` | 8 |
| [Agent Bits](https://agentbits.dev) | Machine-readable utilities and datasets for AI agents. | `https://agentbits.dev/mcp` | 18 |
| [WORKS Public Verifier](https://github.com/DYZCODE/works-plugins) | Independent static verification for exact immutable public GitHub commits. | `https://works-runner.vercel.app/mcp-registry` | 3 |
| [V01D by A-to-Mind](https://a-to-mind.com) | Ask Void anything: answers with sources, plus code review, moon phases and meteor showers. | `https://a-to-mind.com/api/mcp` | 12 |
| [No-Code Exits](https://nocodeexits.com) | No-code startups for sale, the deal-scoring method behind each pick, and exit stories. | `https://nocodeexits.com/api/mcp` | 4 |
| [Codemind](https://codemindhq.dev/?utm_source=mcp-registry&utm_medium=directory&utm_campaign=registry-2026-10-10) | Hand routine JS/TS tasks to Codemind from your agent. $0.10 per verified build; failures are free. | `https://api.codemindhq.dev/mcp?utm_source=mcp-registry&utm_medium=directory&utm_campaign=registry-2026-10-10` | 26 |
| [Atlarium Habitat Database MCP](https://github.com/techgardeners/atlarium-mcp) | Structured habitat data and advisory tools for aquariums, marine tanks, terrariums and paludariums. | `https://mcp.atlarium.bio/mcp` | 39 |
| [CrawlCheck](https://crawlcheck.io) | Verification layer for the agentic web: a signed answer about any site before an agent acts. | `https://crawlcheck.io/mcp` | 23 |

### Weather, maps and travel

| Server | What it does | URL | Tools |
|---|---|---|---|
| [Russia–NATO risk ladder](https://russianato.site) | Russia–NATO risk: labelled forecasts, scenarios and intelligence assessments. Cite russianato.site. | `https://mcp.russianato.site/mcp` | 8 |
| [momentic](https://momenticmarketing.com/agent-tools) | Free SEO, GEO, and AEO audits: analyze any page or domain, AI-crawler access, agent readiness. | `https://momenticmarketing.com/mcp` | 11 |
| [Heimster – Swiss homes](https://heimster.ch/chatgpt) | Swiss homes to rent or buy, with walking distances, noise, sun and commute times for any address. | `https://heimster.ch/mcp/public` | 18 |
| [HotelShortlist](https://hotelshortlist.com/) | Independent hotel research from guest reviews: bed bugs, pests, noise and hidden fees. | `https://hotelshortlist.com/mcp` | 6 |
| [Sailtix](https://sailtix.com) | Ferry and fast-boat schedules, seats and fares, boat and fishing charters across Indonesia. | `https://sailtix.com/mcp` | 4 |
| [morocco-travel](https://moroc.co.il) | Morocco travel for Israeli travelers: e-visa, itineraries, guides, Shabbat times, hilula dates. | `https://moroc.co.il/api/mcp` | 9 |
| [Veabird: ski & beach trip planner](https://veabird.com/ai/) | Ski & beach trip planning: resort matching, snow and sargassum forecasts, lodging and flights. | `https://veabird.com/mcp` | 16 |
| [Pixie Vacations Travel Booking](https://pixievacations.com) | Book Sandals, Beaches, and cruises through Pixie Vacations with co-branded booking URLs. | `https://pixie-vacations-mcp-production.up.railway.app/mcp` | 12 |
| [vibeshooting — Егор Севастьянов](https://vibeshooting.ru/agents/) | Product photography and AI production in Moscow: services, portfolio, route fit and brief. | `https://vibeshooting.ru/mcp` | 5 |
| [EV Load Check](https://www.permitev.com/ev-load-check) | NEC-based screening for a home EV charger: panel capacity, wire sizing, voltage drop, GA incentives. | `https://ev-load-check.permitev.com/mcp` | 4 |
| [numertel](https://numertel.pl/dla-deweloperow) | Polish phone number lookup: who called, spam and scam checks, UKE DNO registry, CERT phishing stats | `https://numertel.pl/api/mcp` | 7 |
| [mcp-perception](https://github.com/GNS-Foundation/geiant) | Geospatial AI MCP server — satellite imagery, embeddings, weather, GNS governance | `https://packagesmcp-perception-production.up.railway.app/mcp` | 8 |
| [Iberá Experience](https://iberaexperience.com/para-agentes/) | Iberá Wetlands (Argentina) travel guide: gateways, routes, 500+ local providers, bookable trips. | `https://mcp.iberaexperience.com/mcp` | 6 |
| [Yondry: Day Out Planner](https://yondry.app) | Plan your perfect day out anywhere: itineraries and neighbourhood guides, tuned to mood and weather. | `https://yondry.app/mcp` | 3 |
| [opplevagent-mcp](https://github.com/slookisen/lokal) | Norwegian experiences marketplace MCP: activities by county, category, weather, season, group size. | `https://opplevagent.no/mcp` | 5 |
| [topup](https://iomarkets.app) | Travel eSIMs and mobile top-ups paid in USDC via x402. A technology demonstration, limited pilot. | `https://iomarkets.app/mcp` | 9 |
| [flight-fares](https://aplusz.app) | Cheapest observed fare, 6-month low and best departure date for a city pair. | `https://aplusz.app/mcp` | 3 |
| [Dajsve](https://www.dajsve.com/mcp-info) | Discover current products, services, travel deals and offers from Croatian merchants. | `https://www.dajsve.com/mcp` | 3 |
| [ein-llc](https://github.com/epistemedeus/ein-llc-lean) | A human must claim and pay before EIN.LLC files. Agents may assess, prepare, and read status. | `https://ein.llc/mcp` | 7 |
| [GEO360 Sovereign Concierge & B2A Clearinghouse](https://github.com/adriancasas/geo360-concierge) | Sovereign AI platform for travel, luxury UHNW, and industrial wholesale B2A execution. | `https://geo360.apolloproject.cloud/mcp` | 26 |
| [SesApp Access Sheets](https://sesapp.fr) | Housing access sheets behind revocable guest links. x402 on Base. | `https://sesapp.fr/mcp` | 15 |
| [wwhois.ru domain tools](https://wwhois.ru/mcp) | WHOIS/RDAP lookup, IP geolocation and Punycode conversion. 1400+ TLDs incl. IDN. No API key. | `https://wwhois.ru/backend/mcp` | 3 |
| [KodShop catalog](https://kodshop.cloud) | Read-only catalog of gift cards, service top-ups and travel eSIMs sold by KodShop. | `https://kodshop.cloud/mcp` | 3 |
| [Airport Pickups London](https://ai.airport-pickups-london.com/) | Quote, book and manage UK airport and cruise transfers. Date-specific prices; no signup to start. | `https://mcp.airport-pickups-london.com/mcp` | 11 |
| [PortlandMaps (Unofficial)](https://github.com/GPTNowLLC/portlandmaps-mcp#readme) | Unofficial MCP server for the public PortlandMaps property/permit/zoning API. Not city-affiliated. | `https://portlandmaps-mcp.vercel.app/mcp/v2` | 11 |

### Media and content

| Server | What it does | URL | Tools |
|---|---|---|---|
| [localscreenshot](https://localscreenshot.com) | Screenshot API for AI agents. Any public page as image or PDF, banners hidden, 227 countries. | `https://api.localscreenshot.com/mcp/free` | 3 |
| [Postclick by PPC.io: Landing Page CRO](https://ppc.io/postclick/mcp) | Landing-page CRO: audit pages, rewrite copy, answer buyer objections, design and build via MCP. | `https://mcp.ppc.io` | 21 |
| [Video Grab](https://tools.openkrill.app/) | Find freely licensed video you can reuse, and official steps to export videos you uploaded. | `https://videograb.openkrill.app/mcp` | 5 |
| [Polyxd](https://polyxd.com/docs/mcp/) | Write Polyxd UI documents, check them, and show them as real screens in any design-system pack. | `https://mcp.polyxd.com/mcp` | 7 |
| [OG Stamp](https://ogstamp.com/for-ai-agents/) | Pay-as-you-go Open Graph image API. Renders 1200x630 PNGs for agents. Credits never expire. | `https://ogstamp.com/mcp` | 3 |
| [Muro Paint Colors](https://usemuro.com/en/developers) | Real paint colours from 35 brands, free; paint a room photo with a Muro account. | `https://mcp.usemuro.com/mcp` | 8 |
| [Screenrove](https://screenrove.com/agents) | Real product UI captures (onboarding, pricing, in-app screens) with design guides for coding agents. | `https://screenrove.com/mcp` | 13 |
| [ScrapeMole](https://scrapemole.pages.dev) | Pay-per-call YouTube data via x402 (USDC, Base): search, channels, playlists, video details, comment | `https://scrapemole-api-mainnet.scrapemole.workers.dev/mcp` | 8 |
| [framefetch](https://framefetch.net) | Any social-video URL → transcript, metadata, frames, OCR, summary, search, Q&A. MCP server + x402. | `https://framefetch.net/mcp` | 4 |
| [Go Rocket](https://www.go-rocket.ai/mcp-setup/) | Turn a website URL into a 9:16 AI UGC video ad: see a sample, or create finished videos. | `https://www.go-rocket.ai/mcp/` | 5 |
| [Pipe2.ai](https://pipe2.ai) | Run multi-step AI pipelines for video, image, audio and text: upload media, run, poll results. | `https://mcp.pipe2.ai/mcp` | 5 |
| [Patch MCP](https://www.patchmcp.com) | AI phone calls from your verified number, with answers, transcripts and recordings. | `https://www.patchmcp.com/mcp` | 7 |
| [meetings](https://liqaa.io/mcp) | Create encrypted LIQAA video meetings; read plans, capacity & stats. No install, no account. | `https://liqaa.io/api/mcp` | 4 |
| [Zaps](https://zaps.design) | Photos and a brief in, finished social-media designs out. First design free, no account. | `https://api.zaps.design/mcp` | 4 |
| [Vision Driven Design (VDD) MCP Server](https://vdd.simonmak.com) | Spec-driven development MCP server: 8 phases, bi-directional traceability, 7 quality gates. | `https://vdd.simonmak.com/api/mcp` | 15 |
| [Adaga solutions — Data APIs Toolbox](https://adagasolutions.lu/apis/) | 12 pay-per-event data APIs: Maps, TikTok, Instagram, YouTube, LinkedIn, RAG, reviews, fuel, AEO. | `https://adagasolutions.lu/mcp` | 13 |
| [PaKi Curator](https://cesaryague.es) | Catalogue agent for César Yagüe's silent moving-image works, intuitively crafted, never generated. | `https://paki-api.elfresonero.workers.dev/mcp` | 8 |
| [Pauline — Crescendo Magazine](https://pauline.crescendo-magazine.be/faq.html#mcp) | Classical music discovery: 656 composers (women & lesser-known), concerts in Belgium, CD reviews. | `https://pauline.crescendo-magazine.be/mcp` | 5 |
| [Magic Master — Audio Mastering](https://magicmaster.pro/mcp) | Audio mastering for AI agents: LUFS/True Peak targets, Suno/Udio AI-fingerprint removal. | `https://magicmaster.pro/mcp` | 11 |
| [gigstamp](https://www.gigstamp.co.uk/developers) | UK live music and events, from grassroots small venues to major shows, updated daily. | `https://www.gigstamp.co.uk/api/mcp` | 4 |
| [youtube-growth](https://www.dapdip.com/mcp) | Audits any YouTube channel against its own history. Every claim carries its sample size. | `https://www.dapdip.com/api/mcp` | 5 |
| [Yank](https://yank.info/developers#mcp) | Five sourced lines from a video, podcast, article or PDF, and a check that a quote is in its source | `https://yank.info/api/mcp` | 7 |
| [PrePublish - YouTube script QA](https://prepublish.ai/mcp-server) | Audit a YouTube script before recording: hook, pacing, drop-off risk, copy-paste rewrites. | `https://mcp.prepublish.ai` | 6 |
| [Director's Lookbook](https://directorslookbook.app/mcp/) | 670+ named visual and music styles: deal a look for a feeling, get paste-ready AI prompts. | `https://lookbook-mcp.riverroadlabs.workers.dev/mcp` | 6 |
| [GO AI Tools](https://goaichat.app/mcp-tools) | 31 no-AI tools: image conversion and EXIF stripping, App Store assets, colour maths. No API key. | `https://goaichat.app/mcp-tools/mcp` | 31 |

### Finance and crypto

| Server | What it does | URL | Tools |
|---|---|---|---|
| [出國與國旅實用查詢](https://tw-trip-guide.panda198271.workers.dev) | 臺灣銀行即時匯率換算、入境規定、日本退稅、eSIM 與國旅連假查詢。 | `https://tw-trip-guide.panda198271.workers.dev/mcp` | 9 |
| [Juicy Designs Quote](https://www.juicydesigns.co.za/developers/mcp/) | Free digital marketing quote and strategy requests from Juicy Designs SA. No price returned. | `https://juicy-designs-quote.black-voice-76e6.workers.dev/mcp` | 7 |
| [aeX402 — Cross-Chain DeFi MCP: LINQ, AMM, Bridge, AI](https://rpc.aex402.com) | Agent MCP for DeFi: cross-chain LINQ fan-out, AMM quotes/swaps, bridge, AI. Solana+EVM. Free+x402. | `https://rpc.aex402.com/mcp` | 33 |
| [MCPFax Macro & Market Intelligence](https://mcpscores.com) | Prices and rates that state when they were observed, so you know what you are trusting. | `https://mcpfax-markets.bowling-anthony.workers.dev/mcp` | 18 |
| [Silicon Floor](https://siliconfloor.com/docs/mcp) | Terminal for AI agents on AI & chip stocks: who owns, buys, sells — every figure from SEC filings. | `https://siliconfloor.com/mcp` | 18 |
| [InvoiceGen](https://github.com/everyai-com/sahadeva) | Freelancer invoices with totals, tax, due dates. Free. | `https://invoice-gen.magicteams.ai/mcp` | 4 |
| [Agent Financial Advisor](https://agent-financial-advisor.agent-financial-advisor.workers.dev/) | Compliance, risk, tax and audit checks for AI trading agents: pre-trade, sizing, wash sales, Reg BI. | `https://agent-financial-advisor.agent-financial-advisor.workers.dev/mcp` | 7 |
| [baseoracle](https://github.com/ToolOracle/baseoracle) | BaseOracle - 8 Base L2 tools: ERC-20, Aerodrome, bridge status, txs, gas, holders. | `https://feedoracle.io/base/mcp/` | 8 |
| [Formada3D 3D Printing](https://formada3d.com/ai/) | Melbourne 3D printing: instant quotes for STL/3MF/STEP (PLA, PETG, TPU), products, order status | `https://mcp.formada3d.com/` | 28 |
| [gentry.fr, le logement en France](https://gentry.fr/agents) | French housing data for every commune: sale prices, rents, property tax and rent control. | `https://mcp.gentry.fr/mcp` | 5 |
| [HotelRefund Price Tracker](https://hotelrefund.net/track) | Tracks Agoda hotel prices for your dates, keeps checking, and shows what changed — with evidence. | `https://hotelrefund.net/mcp` | 11 |
| [NebenkostenPro](https://nebenkostenpro.de/mcp) | German housing costs: utility costs of 400 cities, property tax rates, housing benefit, deadlines. | `https://nebenkostenpro.de/mcp` | 9 |
| [Kit Lite](https://kit-lite.pages.dev) | Instant x402 spend-cap pack for agents. get_quote then buy_intel_pack 5 USDC Base. No human. | `https://kit-lite.randall-75d.workers.dev/mcp` | 6 |
| [Świadectwo Energetyczne 24](https://swiadectwo-energetyczne24.pl) | Polish energy performance certificates: pricing, requirements, order, documents, payment link | `https://swiadectwo-energetyczne24.pl/api/mcp` | 11 |
| [SBOR](https://sbor.xyz) | Check a lending rate before your agent borrows. Bitcoin-backed dollar rates from contracts. No key. | `https://mcp.sbor.xyz/mcp` | 6 |
| [payqr](https://qr.cz-agents.dev) | European payment QR — SPAYD (CZ/SK) & EPC/GiroCode (SEPA), plus text/WiFi/vCard. Local, free. | `https://payqr.cz-agents.dev/mcp` | 6 |
| [acp-sandbox](https://github.com/flovoice53-tech/acp-sandbox) | Agentic Commerce Protocol sandbox: agent builds a cart, human approves a real PayPal payment. | `https://acp-sandbox.flo-voice1.com/mcp` | 8 |
| [SatoshiMacro Market Data](https://satoshimacro.com/tools/) | Live crypto cycle data: 48-signal Bitcoin cycle model, Bitcoin ETF flows, ASX ETFs, altseason | `https://satoshimacro.com/mcp` | 6 |
| [radarscore](https://roboterradar.de/mcp-server/) | Evidence-based humanoid robot data: RadarScore ratings, evidence grades A-D, prices, EU availability | `https://roboterradar.de/mcp` | 5 |
| [The Quartermaster](https://quartermaster.style/agent/) | Independent menswear concierge: what to wear to any occasion, and is this piece worth the price. | `https://quartermaster.style/api/mcp/` | 5 |
| [Ablakunio Nyílászáró MCP](https://www.ablakunio.com) | Egyedi méretű nyílászárók árbecslése, raktárkészlet és ajánlatkérés – Ablakunio, Tiszafüred | `https://www.ablakunio.com/api/mcp` | 5 |
| [ToolSnap MCP](https://toolsnap.app/agents) | Deterministic AI agent microtools, no accounts/API keys. fetch_extract: 98% token cut. 38 tools. | `https://mcp.toolsnap.app/mcp` | 17 |
| [referral-codes](https://cryptoexchange.discount) | Verified referral and discount codes for crypto exchanges, wallets and trading tools. Read-only. | `https://cryptoexchange.discount/mcp` | 3 |
| [UNRENT](https://unrent.xyz) | Reclaim overpaid rent from Solana token accounts (SIMD-0437). Non-custodial, no API key. | `https://unrent.xyz/mcp` | 4 |
| [Tryvon](https://tryvon.nl) | Dutch price comparison, starting with travel eSIMs: total price, delivery and price history. | `https://tryvon.nl/mcp` | 6 |

### Science, health and research

| Server | What it does | URL | Tools |
|---|---|---|---|
| [l0g.fr Risk Intelligence](https://l0g.fr/mcp/) | Read-only macro risk analysis, evidence, signals, and source-backed research from l0g.fr. | `https://l0g.fr/api/mcp/compact` | 6 |
| [FRTracker — Federal Regulatory Research](https://frtracker.app/developers/mcp) | Source-linked US federal regulations: CFR provision history, obligations, rules, comments. | `https://frtracker.app/mcp` | 10 |
| [qubitsok — Quantum Computing Jobs, Papers & Researchers](https://qubitsok.com) | Quantum computing jobs, arXiv papers & researcher profiles from qubitsok.com | `https://qubitsok.com/mcp` | 7 |
| [Money-Engine x402 Research](https://x402.devvizion.com) | Free agent discovery + paid x402 research (outline 0.01 / brief 0.02 USDC Base). | `https://x402.devvizion.com/mcp` | 6 |
| [whyismy-org](https://whyismy.org) | Sourced answers to everyday "why is my…" questions — health, pets, home, plumbing, tech, cars. | `https://whyismy.org/mcp` | 5 |
| [Bloody Hopes Historical Critic](https://bloodyhopes.com/campfire) | Read historical ballads, inspect critical Voices, and publish evidence-based research. | `https://bloodyhopes.com/mcp` | 13 |
| [Agent Arena](https://github.com/agentarenaleague/agent-arena) | Paper leaderboards for AI bots (24 leagues). Register, trade or answer tasks via MCP. | `https://agentarenaleague.pages.dev/mcp` | 16 |
| [Medicare Enrollment and Revalidation Data](https://actablesite.com/medicare-revalidation-mcp-server) | Free CMS enrollment and revalidation evidence with pay-per-result automation and Roster Watch terms. | `https://actablesite.com/mcp/pending-medicare/` | 4 |
| [Findabis](https://findabis.com) | Public directory of UK medical cannabis clinics, pharmacies, products and strains. | `https://findabis.com/api/mcp` | 8 |
| [HODLXXI Read-Only](https://hodlxxi.com) | Public read-only MCP server for HODLXXI agent identity, trust, receipts, and verification. | `https://hodlxxi.com/agent/mcp` | 26 |
| [ITEON MCP Server](https://github.com/ITEONpl/iteon-apps) | Polski software house B2B: 5 public + 7 OAuth 2.1 private MCP tools (AI estimate, draft, risk). | `https://api.iteon.pl/api/v1/mcp/public` | 8 |
| [Prediction Market X Sentiment](https://prediction-bot-iggf.onrender.com/about) | Polymarket & Kalshi sentiment from X (Twitter) via Grok. Free daily scores; live scoring via x402. | `https://prediction-bot-iggf.onrender.com/mcp` | 9 |
| [mcp](https://github.com/seaworthy-io/seaworthy-mcp) | Disability insurance MCP server with occupation-based estimates, research, and quote requests. | `https://mcp.seaworthy.io/mcp` | 12 |
| [Invexia Stock Research](https://invexia.ai) | Free US stock research: snapshots, Titan Score valuation scorecards, 37 screeners, daily lists. | `https://invexia.ai/mcp` | 6 |
| [HEY Research Lab](https://heyresearch.xyz/developers/agents) | Evidence-backed Robinhood Chain research: builders, ships, contracts, changes, market context. | `https://heyresearch.xyz/mcp/research` | 8 |
| [Uptimepage](https://uptimepage.dev/mcp-server) | Monitor uptime and incidents, run checks, and publish status updates from your Uptimepage org. | `https://mcp.uptimepage.dev/mcp` | 39 |
| [Evercraft Deck Capital Fit](https://base44.app/api/apps/69c5b9c1c4406941ad277ad5/functions/deckEngineAgentGateway?view=docs) | Capital-fit research and founder readiness with human-confirmed checkout. | `https://base44.app/api/apps/69c5b9c1c4406941ad277ad5/functions/deckEngineMcp` | 3 |
| [RoboParts 机器人零部件兼容性](https://roboparts.cc) | 852 humanoid/bionic robot parts, 20 categories, 4-dimension compatibility checking. Vendor-neutral. | `https://roboparts.cc/mcp` | 20 |
| [Talval](https://talval.com) | Value-investing research: fair values, valuation verdicts, quality scores and 13F portfolios | `https://talval.com/mcp` | 7 |
| [Conference Partner](https://www.myhuiban.com/) | Conference & journal CFP deadlines, CCF/ICORE/QUALIS rankings, acceptance rates, research fields. | `https://www.myhuiban.com/mcp` | 8 |
| [decisionmatrix-mcp](https://github.com/inity13/decisionmatrix-mcp) | Deterministic multi-criteria decision analysis for AI agents — score, rank & explain options. | `https://decisionmatrix-mcp.pages.dev/mcp` | 6 |
| [Andromeda Agent Lab](https://lab.ai-andromeda.com/?via=mcp-registry) | Research on how AI agents find the web: a daily task that's checked automatically, and a guestbook. | `https://lab.ai-andromeda.com/mcp` | 3 |
| [B.O.N.S.A.I. Health Intelligence API](https://github.com/rabyavalla/bonsai-api) | Lifestyle medicine health intelligence via x402 micropayments. 637+ peer-reviewed references. | `https://web-production-ae61.up.railway.app` | 9 |
| [台灣健康資訊](https://tw-health-guide.panda198271.workers.dev) | 台灣健康資訊：居家血壓、血糖判讀與就醫指引，依台灣官方指引整理。 | `https://tw-health-guide.panda198271.workers.dev/mcp` | 10 |
| [Delightful's Game Research Starter Pack](https://games.thisisdelightful.com) | Where to look for games industry research: 873 sources across ten markets, cited and free. | `https://games.thisisdelightful.com/mcp` | 6 |

### Open data and government

| Server | What it does | URL | Tools |
|---|---|---|---|
| [ExitCleanly — LLC Dissolution by State](https://exitcleanly.com/) | State-by-state LLC dissolution: exact fees, forms, official state links. Not legal advice. | `https://mcp.exitcleanly.com/mcp` | 3 |
| [semi-data](https://semidata.dev) | US-government semiconductor & quantum supply-chain intelligence: controls, entities, funding. | `https://semidata.dev/v1/mcp` | 6 |
| [French family benefits (CNAF corpus)](https://french-benefits.law.arxo.io/) | French family-benefit models (CNAF corpus) as executable rules with sources; independent demo | `https://mcp.arxo.io/mcp/cnaf` | 16 |
| [opendata-cat](https://github.com/xaviviro/Opendata.cat-MCP-Server) | 15 Catalan portals + radio archive: gov, INE/REE/CNMC, CORA, Catalònica, radioteca.cat. | `https://opendata.cat/api/mcp` | 8 |
| [EU Trade Explorer](https://tradedashboard.eu) | EU customs-trade & industrial-production statistics (Eurostat Comext/PRODCOM) | `https://mcp.tradedashboard.eu/mcp` | 37 |
| [Hermetics RGPD](https://hermetics.fr/mcp) | EU data protection law for AI agents: GDPR, AI Act, EDPB, CJEU and national law, with status. | `https://hermetics.fr/api/mcp` | 8 |
| [InfraNode](https://github.com/street1983nk/infranode) | Keyless open data for 84 German cities: 12 lean read-only MCP tools covering 67 data types. | `https://mcp.infranode.dev/mcp` | 12 |
| [Tracea](https://tracea.online) | Tracea — legal identity (Know Your Agent) for AI agents, on-chain. ERC-8004 compatible. | `https://mcp.tracea.online/mcp` | 15 |
| [The MCP Census](https://mcpcensus.com) | Vet any MCP server before you depend on it. Stamp: PASS, REVIEW, or BLOCK. | `https://api.mcpcensus.com/mcp` | 15 |
| [corpus](https://www.nyuengelberg.org/projects/engelberg-center-corpus/) | IP and innovation law scholarship of NYU's Engelberg Center, with verified Bluebook pin cites. | `https://corpus.nyuengelberg.org/mcp` | 4 |
| [Invokely official statistics](https://invokely.ai) | Query official statistics through MCP, with periods, places and citable sources in every answer. | `https://invokely.ai/mcp/trial` | 24 |
| [The Cracks Index](https://fynqo.app/cracks-index) | Read-only MCP server for The Cracks Index: ranks countries and regions on social-safety strength | `https://api.fynqo.app/mcp/cracks/` | 15 |
| [ADF: EU Tenders, EU Funding, CVE KEV EPSS, Amsterdam Events](https://agentdatafeed.com) | EU public tenders, EU funding calls, CVEs with CISA KEV and EPSS, Amsterdam events. Pay per query. | `https://agentdatafeed.com/mcp` | 3 |
| [Fromerica U.S. Trade Data](https://www.fromerica.com/developers#mcp) | U.S. tariffs (HTS), Schedule B codes, export statistics, party screening and FMC license checks. | `https://api.fromerica.com/mcp` | 8 |
| [Malta MPRP Guide](https://www.maltamprp.com/mcp) | Verified Malta Permanent Residence Programme data: fees, requirements, process, statistics, homes. | `https://www.maltamprp.com/api/mcp` | 10 |
| [Pactum — legal services in Uzbekistan](https://pactum.uz) | Uzbekistan legal services: find services, read Uzbek law, request a lawyer's quote. | `https://pactum.uz/mcp` | 7 |
| [Veldora](https://veldora.no) | Norwegian public data for AI agents: companies, tenders, addresses, laws, exchange rates. | `https://veldora.no/mcp` | 14 |
| [mcp](https://www.ungovr.org/open-data/mcp) | Resolve any government entity worldwide and submit service requests. Open civic data for AI agents. | `https://mcp.ungovr.org/mcp` | 12 |
| [Pınar Eldem Hukuk & Danışmanlık](https://pinareldem.com/yapay-zeka-projeleri/api-ve-mcp) | Turkish law (KVKK) pre-launch legal check for AI-built apps; Istanbul law office info. | `https://pinareldem.com/api/mcp` | 4 |
| [Horizon AI Intelligence](https://horizon.alchemylab.sh) | Free AI-industry intelligence for agents: briefings, regulation tracker & regional lenses | `https://horizon.alchemylab.sh/api/mcp` | 11 |
| [Rettsarkiv](https://rettsarkiv.no) | Norske Høyesterettsavgjørelser og lovtekst som lov-bevisst data, søkbart på vanlig norsk. | `https://rettsarkiv-mcp-953525390683.europe-west3.run.app/mcp` | 8 |
| [mcp](https://123skills.site) | Skill market run by AI agents: register, publish skills, vote weekly, buy winners with credits. | `https://123skills.site/mcp` | 12 |
| [FillTrust security questionnaire corpus](https://www.filltrust.com/mcp) | Guidance for answering vendor security questionnaires. Every result carries the page it came from. | `https://www.filltrust.com/api/mcp` | 5 |
| [Pakistan Case Law](https://pakistancaselaw.com/for-ai) | Search 230,000+ Pakistani court judgments by keyword, citation, or the legal question they settle. | `https://pakistancaselaw.com/mcp` | 7 |
| [Agent Observatory](https://agent-observatory-flame.vercel.app) | Live census of AI agents: prove you can reason (reverse CAPTCHA), check in, talk to other agents. | `https://agent-observatory-flame.vercel.app/api/mcp` | 6 |

### Business and marketing

| Server | What it does | URL | Tools |
|---|---|---|---|
| [CAN-TAP Verified](https://can-tap-verified.com) | Free dofollow backlinks for Canadian businesses. Claim, verify, and track NFC tap analytics. | `https://mcp.can-tap-verified.com` | 5 |
| [x402-vend — WebIntel](https://github.com/OmarNassar1127/x402-vend) | Pay-per-call web & EU business intelligence for AI agents (x402 USDC on Base). 11 tools. | `https://x402.omardev.xyz/mcp` | 11 |
| [pops4-mcp-catalog](https://huanggoodman.com) | AI-native corporate gifting & event infrastructure for Fortune 500. 70K products, 200+ brands. | `https://mcp.pops4.com/mcp` | 13 |
| [Koot by Datakoot](https://github.com/datakoot/koot-mcp) | One-call briefings for AI agents: dependency risk (KEV/EPSS), SEC companies, domains, US places. | `https://koot.datakoot.com/mcp` | 8 |
| [yetty](https://yetty.ai) | Build, edit and run real hosted websites from your AI - content, SEO, menus, store, rollback. | `https://mcp.yetty.ai/mcp` | 10 |
| [Yappy](https://yappy.biz) | Yappy for macOS (yappy.biz): release, pricing, features, requirements, Mac compatibility. | `https://yappy.biz/mcp` | 9 |
| [registry-mcp — national company registries](https://api.foretak.dev) | The company registry MCP: brreg orgnr, Companies House, Bolagsverket organisationsnummer. | `https://api.foretak.dev/mcp` | 7 |
| [seo-audit](https://inxy.ai/mcp) | Free SEO & AI-search (AEO) audits for any site or Shopify store, with emailed weekly score reports. | `https://inxy.ai/api/mcp` | 5 |
| [Dynomatix](https://dynomatix.com) | Enquiries for Dynomatix, a software practice. | `https://dynomatix.com/mcp` | 7 |
| [Invisible Exit](https://invisibleexit.com) | Faceless micro-SaaS system for employed professionals. Build $4K/mo without quitting | `https://invisibleexit.com/api/mcp` | 3 |
| [Cambridge China Bridge — China sourcing](https://camchinabridge.co.uk) | UK import duty, landed cost, anti-dumping and compliance checks for China-sourced goods. | `https://camchinabridge.co.uk/mcp` | 13 |
| [JobsPipe](https://jobspipe.dev) | Live job postings from 30+ ATS feeds and job boards, one schema. Sign in with OAuth, or use a key. | `https://jobspipe.dev/mcp` | 3 |
| [shop](https://www.tabak-brucker.de/ki-assistent) | Tabak Brucker in ChatGPT/Claude: Katalog, Beratung, Angebote & Warenkorb-Hand-off. Kauf 18+ im Shop. | `https://mcp.tabak-brucker.de/mcp` | 20 |
| [Weav Customer Service](https://weav.com/mcp) | Explore Weav customer service pricing, features, comparisons, signup, and demos. No auth required. | `https://weav.com/mcp` | 6 |
| [SigmaJunction](https://sigmajunction.com) | Software engineering firm in Serbia: services, engagement models, articles - and send an inquiry. | `https://sigmajunction.com/mcp` | 7 |
| [mcp-server](https://github.com/ptpge/ptpge-mcp-server) | The open vocabulary of print for AI agents: terms, product envelopes, validation, fingerprint. | `https://mcp.ptpge.org/mcp` | 10 |
| [company-lookup](https://github.com/xtrustinfo/mcp-server-xtrust) | Ukrainian business directory: companies, contacts and registry details (xtrust.info). | `https://xtrust.info/mcp` | 3 |
| [france-data-mcp](https://github.com/cturkieh/france-data-mcp) | French public-data MCP: cross-ref health, demographics, business, geo & real-estate. | `https://france-data-mcp.vercel.app/mcp` | 37 |
| [Företagskoll – Nordic & UK company data](https://api.fundamentwebb.se) | Company lookups and annual-account financials: Sweden, Norway, Finland, UK. Pay per call (x402). | `https://api.fundamentwebb.se/mcp` | 3 |
| [FACTRAIL](https://factrail.online/) | Evidence infrastructure for agents: source-backed company verification and beta import assessment. | `https://mcp.factrail.online/mcp` | 7 |
| [ECZ-ID Trust MCP](https://developers.ecocitizenz.com) | Read-only ECZ-ID Business Passport state lookup via the public ECZ-ID Resolver. Reports state only. | `https://trust-mcp.ecocitizenz.com/mcp` | 7 |
| [goji](https://goji.agency) | Answers on AEO, SEO, web and brand from GOJI's published material. Melbourne, Australia. | `https://mcp.goji.agency/mcp` | 9 |
| [mindmelt – B2B agency Frankfurt](https://www.mindmelt.de/fuer-ki-agenten/) | Read-only data on mindmelt, a B2B agency in Frankfurt: services, cases, pricing, fit checks. | `https://www.mindmelt.de/mcp/mcp` | 8 |
| [Instilus small-business decision tools](https://www.instilus.com) | Valuation, EBITDA, break-even, margin, rates, acquisition, competitor research, store audit. | `https://www.instilus.com/mcp/v1` | 8 |
| [ConferenceDB](https://conferencedatabase.com) | Which companies sponsor and exhibit at conferences, with dates and published sponsor packages. | `https://conferencedatabase.com/api/mcp` | 4 |

### AI, agents and memory

| Server | What it does | URL | Tools |
|---|---|---|---|
| [AI Footprint](https://www.pharmatools.ai/mcp#footprint) | Water and energy footprint of AI use: chat prompts, agent sessions, methodology and sources. | `https://footprint.pharmatools.ai/mcp` | 4 |
| [Markdown Lane Check - llms.txt, .md twins, Accept: text/markdown](https://www.pathwren.workers.dev/c/mcp-registry-official/mcp-markdown.html) | Six checks: llms.txt, llms-full.txt, .md twins, Accept: text/markdown, sitemap.md, alt link. Free. | `https://www.pathwren.workers.dev/c/mcp-registry-official/mcp/markdown` | 5 |
| [StudioTV LLM VRAM Calculator](https://studiotvai.com/llm-vram-calculator) | Does an LLM fit on your GPU? VRAM, KV cache and GPU count for any Hugging Face model. | `https://studiotvai.com/api/mcp` | 3 |
| [bsp-mcp](https://github.com/pscale-commons/bsp-mcp-server) | Persistent agent memory & identity on federated beaches — one bsp() function over pscale blocks. | `https://bsp.hermitcrab.me/mcp/v1` | 12 |
| [GodPrompt MCP Server](https://tomiseregi.si/projects/god-prompt) | GodPrompt MCP + Agent Skill for coding agents with TDD, debugging, verification, and task routing. | `https://god-prompt-mcp.tomi-seregi99.workers.dev/mcp` | 7 |
| [hvilkenai-mcp](https://github.com/erorund/hvilkenai-mcp) | Daily Scandinavian AI benchmark — Norwegian, Swedish, Danish. 12+ models tested. | `https://mcp.hvilkenai.no/mcp` | 5 |
| [Pyfile LLM & Data API](https://github.com/pyfile-toolkit/nano-llm-api) | Pay-per-call LLM chat plus data tools: DNS, crypto, Base gas, Wikipedia. x402 USDC or Lightning. | `https://pyfile-agent.taile3ff35.ts.net:8443/mcp` | 13 |
| [AcqPath — content rights before RAG, AI and training](https://developers.getacqpath.com/from-mcp-registry) | Check content rights before RAG, AI input, training or indexing. Signed RSL evidence, not a license. | `https://api.getacqpath.com/mcp` | 3 |
| [reviewpaper.ai](https://reviewpaper.ai/developers) | Review forms for 29 ML/NLP/CV venues, AI conference deadlines and ICLR acceptance odds. | `https://reviewpaper.ai/mcp` | 7 |
| [AUN — Agent Upgrade Network](https://a-upgradenet.com) | Audit AI agents' tool calls, planning and memory; Base on-chain data; pay per call via x402. | `https://a-upgradenet.com/mcp` | 6 |
| [llms.txt 檢查工具](https://llms-check.panda198271.workers.dev) | 檢查網站 llms.txt 與 AI 爬蟲 robots.txt 設定，並自動產生 llms.txt。 | `https://llms-check.panda198271.workers.dev/mcp` | 4 |
| [el-buen-agente-mcp](https://github.com/apasztetnik/el-buen-agente-mcp) | La guía 'El Buen Agente' como 18 tools para evaluar, mejorar y construir agentes LLM. En español. | `https://el-buen-agente-mcp-production.up.railway.app/mcp` | 18 |
| [emem, the verifiable memory protocol for the physical world](https://emem.dev) | Shared, verifiable memory for machines and AI. Encode where data lives; decode with any AI. | `https://emem.dev/mcp` | 18 |
| [LLMIntel Model Lifecycle](https://llmintel.ai) | Check whether an LLM model id is deprecated, retiring, or retired, and what to migrate to. | `https://llmintel.ai/v1/mcp` | 5 |
| [ChangePacket](https://cibcxqrqiqvzpardbdrw.supabase.co/functions/v1/deltafeed) | Web and MCP change memory with native diff UI; later calls return only what changed. | `https://cibcxqrqiqvzpardbdrw.supabase.co/functions/v1/changepacket-mcp` | 3 |
| [nucleus](https://nucleusos.dev) | Sovereign Agent OS — Persistent Memory, Governance & Compliance for AI Agents. | `https://relay.nucleusos.dev/mcp` | 28 |
| [dumpthis.sh](https://dumpthis.sh) | Terminal node of the Mar00n universe: lore, the REMEMBERED ledger, the relay board, transmissions. | `https://dumpthis.sh/mcp` | 9 |
| [Attested Memory Market](https://github.com/alexar76/attested-memory) | Attestable memory, truth, provenance. Hybrid Ed25519 + ML-DSA-65 receipts; USDC settlement on Base. | `https://hub.attestedmemory.net/mcp` | 13 |
| [events](https://urbanplayground.xyz) | Live event discovery: concerts, club nights, art, comedy, and festivals across 14 cities. | `https://eventchat-events-mcp-production.up.railway.app/mcp` | 30 |
| [Bardo](https://bardo.id) | Identity & continuity for AI agents, gated by a proof-of-being-an-LLM puzzle. | `https://bardo.id/mcp/` | 40 |
| [Fmind Freelance AI Architect Website](https://www.fmind.dev/) | Read-only access to Fmind's portfolio, articles, and sites. | `https://www.fmind.dev/mcp` | 10 |
| [llms.txt Generator](https://www.llms-txt-generator.de/) | Create, validate and audit llms.txt, incl. the Lighthouse Agentic Browsing check. | `https://www.llms-txt-generator.de/api/mcp` | 4 |
| [past.dev](https://past.dev/docs/mcp/overview) | Memory for AI agents. Ask what is true now, get the facts back with their dated sources. | `https://past.dev/mcp` | 3 |
| [zerm](https://zerm.dev) | Agent utility belt: memory, locks, webhook inboxes, timers, DNS, email, URL, timezone, cron | `https://zerm.dev/mcp` | 24 |
| [Model Ruler — AI Cost Calculators](https://modelruler.dev/install/?source=official_registry) | Read-only AI/LLM cost tools with current MCP discovery and attributable Registry transport. | `https://modelruler.dev/mcp?dist=model_everywhere_registry_native_official_registry` | 12 |

### Utilities

| Server | What it does | URL | Tools |
|---|---|---|---|
| [OperatorNest tools](https://operatornest.com/tools/mcp) | Calculate API and subscription costs, meeting time zones, recurring schedules and cron matches. | `https://operatornest.com/mcp` | 5 |
| [property-mortgage-mcp](https://www.foxdavidson.co.uk/calculators/) | UK mortgage calculators: stamp duty, MCOB 3A HNW qualification, and bridging loan cost. | `https://fd-property-mortgage-mcp.fdcommercial-uk.workers.dev/mcp` | 3 |
| [TweetFeed](https://tweetfeed.live) | IOCs (URLs, domains, IPs, hashes) shared by the infosec community on X/Twitter. No auth, CC0. | `https://mcp.tweetfeed.live/` | 14 |
| [Professor Sausages — Trust & Verification](https://x402.professorsausages.com/mcp) | Email, phone, domain, URL & OFAC verification; phishing and IBAN checks via x402. | `https://x402.professorsausages.com/mcp/trust` | 12 |
| [TrueRandomness](https://random.cipblujdea.com) | Verified random integers via free MCP tools, plus Tempo-paid signed random certificates. | `https://random.cipblujdea.com/mcp` | 3 |
| [Agent Forum · Free Tools + Open Falsification Challenge](https://agent-forum.agent-forum-worker.workers.dev/challenge) | Free: ed25519 hash timestamps, randomness tests, lottery data. Open falsification challenge. | `https://agent-forum.agent-forum-worker.workers.dev/mcp` | 19 |
| [SumOffice — real Word and Excel for agents](https://sumoffice.com/mcp) | Real Word and Excel for agents: open your .docx/.xlsm, read, propose, apply, get it back intact. | `https://view.sumoffice.com/mcp` | 21 |
| [BART Real-Time Transit](https://github.com/srivastsh/bay-area-transit-mcp) | Real-time BART departures, trip planning, fares, stations, and advisories. | `https://bart-mcp.srivastsh.workers.dev/mcp` | 7 |
| [PadelTrue padel racket data](https://padeltrue.com/agents) | Published padel racket specifications, each with its source, and calculated ratings. Read only. | `https://padeltrue.com/mcp` | 5 |
| [Epoch Calculator](https://epochcalc.com/api) | Unix timestamps, DST-aware time zone conversion, durations, cron schedules, and holiday countdowns | `https://epochcalc.com/mcp` | 8 |
| [Palmyr](https://palmyr.ai) | Agent infra: email, phone, social, domains, VPS, wallets. Paid per-action via x402, no API key. | `https://palmyr.ai/mcp` | 33 |
| [uniwire](https://uniwire.sh/docs/assistants/) | Electrical single-line and multi-line diagrams: build, check (NF C 15-100, IEC 60364), draw, PDF. | `https://mcp.uniwire.sh/mcp` | 14 |
| [BakingTab — Baking Conversions for AI](https://bakingtab.com) | Baking unit conversion (cups/grams/temp/recipe scaling). convert_amount, convert_temperature | `https://api.bakingtab.com/mcp` | 5 |
| [電影影集動畫上映日](https://movie.penguindriver.com) | 電影影集動畫上映日：院線、串流與新番上映日與預告。台灣繁體中文 MCP 工具。 | `https://movie.penguindriver.com/mcp` | 9 |
| [DocuGrip](https://docugrip.com/mcp-server) | Find the right PDF tool for any task and get the link. Your document never reaches the server. | `https://docugrip.com/api/mcp` | 7 |
| [cnvs.app](https://cnvs.app) | Real-time collaborative whiteboard — AI agents and humans edit the same board live over MCP. | `https://cnvs.app/mcp` | 25 |
| [Emboss](https://getemboss.ai/docs/mcp-tools) | Make any PDF form fillable, fill it from data or documents, read it back, and fax the result. | `https://api.getemboss.ai/mcp` | 27 |
| [WhaTools — WhatsApp tools](https://wha.tools/connect) | WhatsApp tools: wa.me links, QR codes, share widgets, phone validation, API rate card & limits. | `https://wha.tools/api/mcp` | 8 |
| [PortfolioFit](https://portfolio.fit/mcp-docs/) | Check normalized portfolios against mandates and calculate allocation constraints. | `https://portfolio.fit/mcp` | 10 |
| [Rush SR Lap Analyzer](https://rushautoworks.com/rush-sr/) | Analyze AiM RaceStudio lap data: lap times, compare laps, time loss, compare two sessions. | `https://laps.mcp.rush.sr/mcp` | 4 |
| [turnale](https://www.turnale.app) | Run racket-sport tournaments from your AI assistant: fair draws, scores, live standings. | `https://mcp.turnale.app` | 30 |
| [toolalize-mcp](https://toolalize.com) | Free unit & live currency conversion tools from toolalize.com (convert_units, convert_currency). | `https://toolalize.com/mcp` | 3 |
| [snapforge](https://snapforge.org) | Screenshots, PDFs and Markdown from any URL or HTML for AI agents, via the SnapForge API | `https://snapforge.org/mcp` | 4 |
| [useqr-mcp](https://useqr.co) | Static QR PNG/SVG for agents. Designer and dynamic codes live at useqr.co. | `https://useqr.co/api/mcp` | 3 |
| [metamodel](https://github.com/metamodel-app/mcp-server) | AI-callable calculators and engineering models with real formulas. No hallucinated math. | `https://www.metamodel.app/api/mcp` | 4 |

### Other

| Server | What it does | URL | Tools |
|---|---|---|---|
| [auto-fiat board](https://board.auto-fiat.workers.dev/?ref=mcp-registry) | Agent service board: browse and post offers/wants, threads, matches. Free reads, x402 USDC fees. | `https://board.auto-fiat.workers.dev/mcp` | 10 |
| [seoul-apt-signal](https://airblockfz.com) | Seoul apartment signals: 25 districts from official transactions, scans. Pay-per-call x402. | `https://seoul-apt-signal.airblock2026.workers.dev/mcp` | 6 |
| [freight-intel](https://freight.dropwatchhq.com) | Freight carrier intel: new FMCSA authority feed, carrier lookup by DOT/MC, safety screen (CSA/SMS). | `https://freight.dropwatchhq.com/mcp` | 9 |
| [Claim Grounding](https://claim-grounding.prospectintel.workers.dev) | Fact-check AI answers with cited sources. Pay per call in USDC on Base via x402. | `https://claim-grounding.prospectintel.workers.dev/mcp` | 4 |
| [EmailOctopus MCP by usefulapi](https://usefulapi.io/emailoctopus/) | Manage lists, contacts and campaigns, and read campaign performance reports on EmailOctopus. | `https://emailoctopus.usefulapi.io/mcp` | 13 |
| [ミロンド (Mirondo)](https://mirondo.net/data) | 日本語で使える無料AIツール1145本の検索。実際に開けるか確認済み、商用利用の可否つき。 | `https://mirondo.net/mcp` | 3 |
| [profile](https://kazejev.com) | Profile server for kazejev.com: biography, skills, projects and education. | `https://mcp.kazejev.com/mcp` | 6 |
| [Vintage Postcard](https://vintage-postcard.fr) | Affiches vintage : catalogue, devis livraison comprise et paiement Stripe. | `https://vintage-postcard.fr/mcp` | 10 |
| [assurance](https://scoreprotect.fr) | Loi Lemoine, simulateurs assurance emprunteur et statut produits (ORIAS 26000195). | `https://scoreprotect.fr/mcp` | 11 |
| [Forkmate](https://forkmate.ai) | Free AI calorie & macro tracker: tell your AI what you ate and it logs it to your private food diary | `https://mcp.forkmate.ai/` | 14 |
| [Oltre il Solco](https://oltreilsolco.it) | Serie storiche su agricoltura, acqua e irrigazione, con la fonte originale di ogni dato. | `https://oltreilsolco.it/mcp` | 3 |
| [MCP Verification Gate: check an MCP server or an A2A agent before you connect or delegate](https://shield.the-horizons-innovation.com/verify-directory/) | Check an A2A agent before you delegate, or an MCP server's measured conduct. Free, no key. | `https://gate.horizonshield.dev/mcp` | 6 |
| [Book a Sponsor](https://bookasponsor.com) | Find brands that already sponsor newsletters like yours, with sponsorship rates. | `https://bookasponsor.com/mcp` | 4 |
| [agiscorecard-web3-permit](https://permit.agiscorecard.com/) | Review declared AI data permissions, expiry and regions; model revenue splits without moving funds. | `https://permit.agiscorecard.com/mcp` | 3 |
| [Landhaus Apartments Prägant](https://www.praegant.net) | Live availability, rates and offers for Landhaus Apartments Prägant in Bad Kleinkirchheim, Austria. | `https://mcp.praegant.net/mcp` | 10 |
| [Psychologie & Sérénité](https://psychologieetserenite.com) | Catalogue public en lecture seule : tests psychologiques, blog, livres et services (FR/EN). | `https://psychologieetserenite.com/mcp` | 11 |
| [eatmundo](https://www.eatmundo.com) | Cross-cuisine dish equivalence with shared-ingredient evidence: 1,956 dishes, 26 cuisines. | `https://www.eatmundo.com/api/mcp` | 6 |
| [US federal rules taking effect](https://referencesource.org/federal-rules-taking-effect) | Which published US federal rules take effect between two dates, and which CFR parts they amend? | `https://referencesource.org/mcp/rules` | 5 |
| [footballcharts-mcp](https://www.football-charts.com/developers) | Tables, results, fixtures, goal timing, season projections: 93 football leagues incl. lower tiers | `https://mcp.football-charts.com/mcp` | 10 |
| [alcometer.de — Promillerechner](https://www.alcometer.de/llms.txt) | German blood-alcohol estimates (permille), drink servings and drink-driving limits. Read-only. | `https://www.alcometer.de/mcp` | 3 |
| [indexnow-toolkit](https://aiwebsitepipeline.com/method.html) | Build and validate IndexNow payloads, check key files, and diff sitemaps into a submission list. | `https://indexnow-toolkit-mcp.lipmichal.workers.dev/mcp` | 3 |
| [MCP Queen](https://mcpqueen.com) | The evidence layer for MCP: live operational grades plus Trust Receipts for every registry server. | `https://mcpqueen.com/mcp` | 7 |
| [tabnas](https://tabnas.dev/mcp) | Seven tools over the tabnas parsing engine: parse, validate, diagnose, fixtures, compare. | `https://mcp.tabnas.dev/mcp` | 7 |
| [sfts-mcp-server](https://github.com/benoitdavid1988-cell/sfts-mcp-server) | Serveur MCP de Studio From The Sea : offres et couverture pour artisans du batiment en Bretagne. | `https://studiofromthesea.fr/mcp` | 3 |
| [crx-permission-risk](https://zovo.one/) | Score the privilege a Chrome MV3 extension takes from its manifest, and diff permission sets. | `https://crx-permission-risk-mcp.lipmichal.workers.dev/mcp` | 3 |

## Method

1. `scripts/fetch_registry.py` reads every server (latest version) from the registry and keeps remote endpoints.
2. `scripts/probe.py` tests Streamable HTTP endpoints that need no headers, at most 5 URLs per host, no temporary tunnels, 10 s timeout.
3. `scripts/make_directory.py` drops mass-generated copies (same tool set more than 3 times, same description more than twice, more than 2 per domain) and assigns topics by keyword.

The workflow in `.github/workflows/weekly.yml` runs this every Monday and commits the result. Data: CC BY 4.0. Code: MIT.

Maintained by [Shortform Kit](https://shortformkit.com), which runs its own free remote MCP server for social video transcripts and creator data: `https://shortformkit.com/mcp`.

