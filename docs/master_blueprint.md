# ALPHA LEARNING GAMES — ALPHA QUEST
## COMPLETE MASTER PROJECT PROMPT, SOFTWARE BLUEPRINT & STEP-BY-STEP DEVELOPMENT PLAN

**Project Name:** Alpha Learning Games  
**Flagship Product:** Alpha Quest  
**Tagline:** Learn. Explore. Achieve.  
**Founder:** Iniobong Eyibio  
**Development Credit:** Iniobong Eyibio + AI-assisted development  
**Target Users:** Primary school children aged 6–11  
**Initial Platform:** Responsive web application for desktop computers, tablets, and mobile browsers  
**Primary Backend Language:** Python  
**Frontend:** HTML, CSS, JavaScript  
**Backend Framework:** FastAPI  
**Development Database:** SQLite  
**Production Database:** PostgreSQL  
**Project Type:** Educational adventure game and learning platform

---

# PART 1 — YOUR ROLE AS MY DEVELOPMENT PARTNER

You are my senior software architect, Python developer, educational game designer, UI/UX designer, database architect, software tester, cybersecurity adviser, and personal programming instructor.

Your responsibility is to guide me from an idea to a working, tested, and deployable educational gaming platform called ALPHA LEARNING GAMES, beginning with its flagship product, ALPHA QUEST.

I am learning Python and practical software development. I want to develop this product with your assistance, understand how it works, and gradually become capable of maintaining and expanding it.

Do not treat this as a request for a theoretical document alone. We will use the blueprint to build actual working software.

## Mandatory development rules

1. Follow the master plan in the correct order.
2. Divide development into phases, milestones, and small, verifiable tasks.
3. Do not skip foundational work or jump directly to advanced features.
4. Before writing code for a major feature, explain its purpose, architecture, dependencies, and expected result.
5. Give me exact file paths and complete code for each file we need to create or replace.
6. Clearly state whether code should be added, replaced, or appended.
7. Avoid giving incomplete code fragments when a complete working file is needed.
8. Do not silently change the approved architecture, file structure, database design, or branding.
9. If an architectural change is necessary, explain the reason and ask for my approval before making a major change.
10. Never claim that code has been run, tested, deployed, or verified unless it actually has been.
11. Provide the exact terminal commands needed for installation, execution, and testing.
12. Explain expected output and common errors.
13. Help me diagnose errors from the actual error message rather than guessing.
14. Never expose secret keys, passwords, or private credentials in source code.
15. Use Git and checkpoints where appropriate so we can recover working versions.
16. Keep a development log, a list of completed milestones, outstanding bugs, and next actions.
17. Preserve continuity between sessions using a project status document.
18. Do not introduce unnecessary libraries, subscriptions, paid services, or complex infrastructure.
19. Prefer simple, maintainable, documented code suitable for a beginner to understand.
20. Build the smallest useful version first, then improve it through testing.

## My preferred teaching method

Use this teaching sequence:

**Explain → Show → I type → Run → Check → Modify → Challenge.**

Sometimes provide a complete real-world program for me to type and run. At other times, give me a partially completed program to finish myself.

When I make an error, give useful debugging hints before revealing the full correction, unless I specifically ask you to fix the code directly.

Use practical examples from Alpha Quest and its educational game mechanics.

---

# PART 2 — PRODUCT VISION

ALPHA LEARNING GAMES will be a family of educational games designed to make learning enjoyable, interactive, memorable, and rewarding.

ALPHA QUEST is the first flagship product.

The objective is to create a distinctive learning adventure that competes with established educational platforms such as Blooket and Wayground through its combination of:

- Story-driven educational missions.
- Interactive subject worlds.
- Exploration and discovery.
- Multiple question and puzzle formats.
- XP points, achievements, and collectible rewards.
- A personal virtual building world.
- Adaptive learning and spaced revision.
- Individual and team challenges.
- Teacher-created assignments.
- Learning progress reports.
- Child-friendly design and privacy protection.

Do not merely copy another company's interface, artwork, branding, proprietary content, or game implementation. Create an original product identity and original gameplay systems.

The product should be engaging without sacrificing educational quality.

## Product mission

Help children learn academic subjects through exploration, play, problem-solving, feedback, creativity, and repeated practice.

## Product vision

Build a scalable educational gaming platform that can eventually support multiple games, subjects, teachers, schools, languages, and age groups.

## Target audience

Primary school learners aged 6–11.

Design content and difficulty for different developmental levels. Use adjustable age bands, readable text, simple instructions, accessible interactions, and appropriate learning objectives.

The initial product should work without requiring a native Android or iOS application.

---

# PART 3 — BRAND IDENTITY

Use the following official brand colors consistently.

- Navy: #0A1E3D
- Blue: #1A4B8C
- Gold: #C9A84C
- White: #FFFFFF
- Light Gray: #F4F6F9
- Dark Gray: #2D3748

Product name: ALPHA QUEST.

Parent brand: ALPHA LEARNING GAMES.

Tagline: LEARN. EXPLORE. ACHIEVE.

The interface should feel polished, adventurous, modern, friendly, and premium without becoming visually confusing.

Use colorful illustrated worlds, friendly original characters, attractive mission cards, clear icons, readable fonts, smooth but restrained animation, and well-designed reward screens.

Avoid excessive gradients, flashing effects, unnecessary pop-ups, tiny text, and cluttered layouts.

Keep artwork, interface components, and business logic separate so that visual improvements do not require rewriting the Python game engine.

Use original or appropriately licensed assets. Do not assume that externally sourced images or fonts are free for commercial use.

---

# PART 4 — THE GAME WORLD

Players are called EXPLORERS.

A player chooses a nickname and an approved avatar, then enters the Alpha Quest learning world.

The world is divided into five initial regions.

## World 1: Math World

Topics:

- Counting and number recognition.
- Addition and subtraction.
- Multiplication and division.
- Fractions.
- Shapes and geometry.
- Patterns and sequences.
- Measurement.
- Time and money.
- Age-appropriate mathematical word problems.

## World 2: English Kingdom

Topics:

- Alphabet recognition.
- Phonics and spelling.
- Vocabulary.
- Synonyms and antonyms.
- Grammar.
- Sentence construction.
- Reading comprehension.
- Punctuation.
- Storytelling and writing.

## World 3: Science Lab

Topics:

- Living and non-living things.
- Plants and animals.
- The human body.
- Matter.
- Forces and motion.
- Energy.
- Weather and Earth.
- Space.
- Basic scientific observation and reasoning.

## World 4: Discovery World

Topics:

- Geography.
- Continents and oceans.
- Maps and directions.
- Cultures and communities.
- Historical timelines.
- Landmarks and discoveries.
- Understanding the world.

Ensure that historical and cultural content is reviewed for factual accuracy and respectful representation.

## World 5: Logic Temple

Topics:

- Patterns.
- Sequences.
- Memory challenges.
- Deduction.
- Spatial reasoning.
- Problem-solving.
- Puzzles.
- Critical thinking.

All educational content must be age-appropriate, fact-checked, and reviewed before publication.

Organize the content around explicit skills and learning objectives. Do not assume every child follows the same school curriculum.

---

# PART 5 — SIGNATURE GAMEPLAY

The game should offer a connected adventure rather than a collection of disconnected quizzes.

## Core gameplay loop

1. The Explorer enters a subject world.
2. The Explorer selects an available mission.
3. The mission introduces a story objective.
4. The player completes questions, puzzles, or other learning activities.
5. The system evaluates answers and explains mistakes.
6. The player earns XP and, where appropriate, building resources.
7. The mission records progress.
8. The game recommends an appropriate next mission or revision activity.
9. Completing missions unlocks further content.
10. The Explorer uses earned resources in the Knowledge Builder.

## Game Mode A: Mystery Case

Players investigate a mystery by answering questions, interpreting clues, and solving a final puzzle.

Example: A museum's missing star map can only be recovered by solving mathematics, reading, and logic clues.

The mystery should require understanding rather than random guessing.

## Game Mode B: Brain Rush

A short sequence of arithmetic, spelling, memory, and logic challenges.

Allow untimed and timed variants. Timers must be optional or limited to appropriate activities.

## Game Mode C: Memory Vault

Players revisit previously learned concepts.

Use spaced revision, progressively varied examples, and encouraging feedback.

## Game Mode D: Team Quest

Players cooperate to solve a shared challenge.

Introduce real-time multiplayer only after the single-player experience is stable. Use private rooms, joining codes, server-authoritative scoring, and child-safety controls.

## Game Mode E: Boss Battle

A final multi-step challenge combines skills practiced in previous missions.

Boss battles should reward understanding and persistence, not merely speed.

## Game Mode F: Knowledge Builder

This is the signature feature of Alpha Quest.

Players earn building resources by completing learning missions. They can use these resources to build a home, village, laboratory, library, or other approved structures.

Initially, implement a simple grid or tile-based building interface. Do not begin with complex 3D world rendering.

The system should validate rewards on the server and prevent players from duplicating resources through repeated requests.

---

# PART 6 — REWARDS AND SCORING

Implement an initial scoring system that can be adjusted through configuration.

Provisional rules:

- Correct answer: 20 XP.
- Correct answer using a hint: 10 XP.
- Incorrect answer: 0 XP.
- Completed mission: 25 bonus XP.
- Completed revision activity: 10 bonus XP.

These values are starting points, not permanent rules.

The system must clearly define when XP is awarded, how retries work, and whether a replay can earn the same completion bonus.

Avoid rewarding only speed. Reward accuracy, persistence, improvement, and demonstrated learning.

## Reward types

- XP points.
- Explorer levels.
- Subject badges.
- Mission completion badges.
- Avatar accessories.
- Building materials.
- Building upgrades.
- World unlocks.
- Collection achievements.

Do not create pay-to-win advantages. The free learning experience must remain useful without purchases.

---

# PART 7 — SCREEN-BY-SCREEN UI SPECIFICATION

Build a responsive web interface that works on desktop, tablets, and mobile browsers.

## Screen 1: Welcome

Elements:

- Alpha Quest logo.
- Short introduction.
- Play button.
- Sign-in option where applicable.
- Parent or teacher access.
- Accessibility settings.

## Screen 2: Explorer Setup

Elements:

- Nickname selection.
- Avatar selection.
- Age-appropriate experience settings.
- Accessibility preferences.
- Clear explanation of the game.

Do not require a child to enter a real full name, precise location, or unnecessary personal information.

## Screen 3: Home Dashboard

Elements:

- Explorer avatar and nickname.
- Current level and XP progress.
- Subject world map.
- Next recommended mission.
- Daily learning activity.
- Reward preview.
- Knowledge Builder entry.
- Clear navigation.

## Screen 4: World Map

Show the five subject regions as distinct, illustrated areas.

Each region should show:

- Subject name.
- Current progress.
- Available missions.
- Locked missions.
- Completed missions.
- Clear unlock requirements.

Do not use color alone to distinguish locked, completed, and available regions.

## Screen 5: Mission Briefing

Elements:

- Character or guide.
- Mission title.
- Short story.
- Learning objective.
- Estimated duration.
- Reward preview.
- Start button.

## Screen 6: Challenge Room

Elements:

- Mission progress.
- Question or puzzle.
- Relevant illustration or audio.
- Large answer controls.
- Hint button where appropriate.
- Submit action.
- Accessible instructions.

Support multiple-choice questions first. Add true/false, ordering, matching, and other formats after the core system is stable.

## Screen 7: Feedback

Elements:

- Correct or incorrect status.
- Correct answer when necessary.
- Short explanation.
- Encouraging language.
- Continue or retry action.

Do not shame players for mistakes.

## Screen 8: Results

Elements:

- Mission completion status.
- XP earned.
- Skills practiced.
- Rewards unlocked.
- Suggested next activity.
- Return to world button.

## Screen 9: Knowledge Builder

Elements:

- Personal building area.
- Grid or tile-based placement.
- Available resources.
- Buildings and decorations.
- Upgrade controls.
- Save progress.

## Screen 10: Rewards Room

Elements:

- Earned badges.
- Collectibles.
- Avatar accessories.
- Achievement explanations.
- Locked reward previews.

## Screen 11: Teacher Studio

Introduce this after the core player experience.

Elements:

- Teacher-managed classrooms.
- Student roster.
- Question bank.
- Mission assignment.
- Assignment results.
- Skill progress reports.
- Exportable reports where appropriate.

## Screen 12: Parent/Guardian Area

Elements:

- Authorized child account management.
- Privacy and consent controls where required.
- Progress overview.
- Data access and deletion options.
- Account settings.

Protect adult-only functions with appropriate authorization and secure authentication.

## Responsive design requirements

Desktop:

- Left navigation.
- Central world map and mission area.
- Compact progress panel.

Mobile:

- Bottom navigation.
- Large touch targets.
- Scrollable subject map.
- Responsive question cards.
- No essential horizontal scrolling.

Accessibility:

- Keyboard navigation.
- Readable text.
- Clear focus indicators.
- Sufficient contrast.
- Captions or text alternatives for important audio.
- Reduced-motion option.
- Screen-reader-friendly controls.

---

# PART 8 — SOFTWARE ARCHITECTURE

Use a modular architecture.

## Frontend

- HTML for structure.
- CSS for styling and responsive layouts.
- JavaScript for interactions, animations, and API calls.

## Backend

- Python 3.
- FastAPI.
- Pydantic for request and response validation.
- SQLAlchemy for database access.

## Database

- SQLite for initial local development.
- PostgreSQL for production deployment.
- Database migrations for schema changes.

## Testing

- pytest for Python unit and integration tests.
- FastAPI test client for API tests.
- Playwright for browser-level end-to-end testing.

## Version control

Use Git. Establish meaningful commits after working milestones.

## Architecture rules

1. Keep game rules independent from the UI.
2. Keep database access separate from API route handlers.
3. Keep educational content separate from source code.
4. Validate important operations on the server.
5. Never trust browser-submitted XP, scores, or unlock claims.
6. Use environment variables for secrets.
7. Document setup and execution commands.
8. Use consistent naming conventions.
9. Add automated tests for critical logic.
10. Avoid unnecessary abstraction during the first version.

## Main backend modules

- `main.py`: application entry point.
- `config.py`: configuration.
- `api/`: HTTP routes.
- `models/`: database models.
- `schemas/`: validated request and response structures.
- `services/scoring.py`: scoring rules.
- `services/learning.py`: learning and revision rules.
- `services/rewards.py`: reward calculations.
- `repositories/`: database operations.
- `db/`: database connection and session management.
- `tests/`: automated tests.

---

# PART 9 — APPROVED PROJECT FOLDER STRUCTURE

Create the following project structure incrementally.

alpha-learning-games/
    README.md
    .gitignore
    .env.example
    requirements.txt

    docs/
        master_blueprint.md
        game_design_document.md
        ui_specification.md
        database_schema.md
        test_plan.md
        project_status.md
        changelog.md

    games/
        alpha_quest/
            backend/
                app/
                    main.py
                    config.py

                    api/
                        health.py
                        subjects.py
                        questions.py
                        missions.py
                        progress.py
                        rewards.py

                    models/
                        player.py
                        subject.py
                        skill.py
                        question.py
                        mission.py
                        progress.py
                        reward.py
                        building.py

                    schemas/
                    services/
                        scoring.py
                        learning.py
                        rewards.py
                        missions.py

                    repositories/
                    db/

                tests/

            frontend/
                index.html

                assets/
                    images/
                    audio/
                    icons/

                css/
                    base.css
                    dashboard.css
                    world_map.css
                    mission.css
                    results.css
                    accessibility.css

                js/
                    api.js
                    dashboard.js
                    world_map.js
                    mission.js
                    results.js
                    knowledge_builder.js

            content/
                math/
                english/
                science/
                discovery/
                logic/

            scripts/
                seed_database.py

    shared/
        design_system/
        documentation/

This structure is the target architecture. Do not generate every file at once.

Start with the minimum necessary files, make them work, and introduce the remaining modules when their milestone begins.

If a simpler structure is more appropriate during the first prototype, explain the difference and preserve a clear path to the approved structure.

---

# PART 10 — DATABASE DESIGN

Create normalized relational database tables with proper primary keys, foreign keys, indexes, constraints, and timestamps.

## Table: players

Fields:

- id.
- nickname.
- avatar_id.
- created_at.
- updated_at.
- account_status.

## Table: guardians

Fields:

- id.
- email, where required.
- authentication reference.
- consent status where applicable.
- created_at.

Avoid retaining unnecessary personal information.

## Table: player_guardians

Fields:

- player_id.
- guardian_id.
- relationship or authorization type where appropriate.

## Table: subjects

Fields:

- id.
- name.
- world_slug.
- description.
- display_order.
- status.

## Table: skills

Fields:

- id.
- subject_id.
- name.
- description.
- grade_band.
- learning_objective.

## Table: questions

Fields:

- id.
- skill_id.
- question_type.
- prompt.
- difficulty.
- explanation.
- content_status.
- created_at.

## Table: answer_options

Fields:

- id.
- question_id.
- label.
- option_text.
- is_correct.

Do not expose answer keys unnecessarily in public question responses.

## Table: missions

Fields:

- id.
- subject_id.
- title.
- description.
- difficulty.
- sequence.
- unlock_requirements.
- status.

## Table: mission_questions

Fields:

- mission_id.
- question_id.
- position.

## Table: attempts

Fields:

- id.
- player_id.
- question_id.
- mission_run_id.
- is_correct.
- used_hint.
- difficulty.
- created_at.

Store only the attempt information needed for learning and reporting.

## Table: mission_runs

Fields:

- id.
- player_id.
- mission_id.
- status.
- started_at.
- completed_at.
- xp_earned.
- completion_bonus_awarded.

## Table: skill_mastery

Fields:

- player_id.
- skill_id.
- mastery_score.
- evidence_count.
- updated_at.

Treat mastery as an estimate, not an unquestionable measurement of a child's ability.

## Table: rewards

Fields:

- id.
- name.
- reward_type.
- description.
- asset_reference.
- eligibility_rule.

## Table: player_rewards

Fields:

- player_id.
- reward_id.
- earned_at.

## Table: buildings

Fields:

- id.
- player_id.
- building_type.
- level.
- position_x.
- position_y.
- created_at.

Add classroom, assignment, and classroom-membership tables in the teacher-feature milestone.

Use database migrations when changing schemas.

---

# PART 11 — GAME ENGINE IMPLEMENTATION

Build the engine in small, testable modules.

## Module A: Question Engine

Responsibilities:

- Load questions from structured data or the database.
- Present appropriate questions.
- Validate submitted answers.
- Return correctness and explanations.
- Support question types incrementally.

## Module B: Mission Engine

Responsibilities:

- Start missions.
- Track mission runs.
- Determine completion.
- Manage unlock requirements.
- Prevent duplicate completion rewards.
- Support retries.

## Module C: Scoring Engine

Responsibilities:

- Calculate XP on the server.
- Apply configured scoring rules.
- Handle hints.
- Handle completion bonuses.
- Prevent score manipulation.

## Module D: Learning Engine

Responsibilities:

- Track evidence of understanding.
- Identify skills needing revision.
- Recommend suitable questions.
- Adjust difficulty gradually.
- Schedule spaced practice.

Begin with simple, explainable rules. Do not claim that a learner has mastered a subject based on one or two answers.

## Module E: Reward Engine

Responsibilities:

- Award badges.
- Unlock approved items.
- Track building resources.
- Prevent duplicate or invalid rewards.

## Module F: Progress Engine

Responsibilities:

- Save mission outcomes.
- Summarize learning progress.
- Track subject and skill performance.
- Provide reports for authorized teachers and guardians.

## Module G: Content Engine

Responsibilities:

- Load approved question banks.
- Validate question formats.
- Organize content by subject, skill, age band, and difficulty.
- Support later localization.

---

# PART 12 — API DESIGN

Introduce APIs gradually.

Initial endpoints:

GET `/health`

Purpose: Check application health.

GET `/api/v1/subjects`

Purpose: Return available subject worlds.

GET `/api/v1/missions`

Purpose: Return available missions, with suitable filters.

GET `/api/v1/missions/{mission_id}`

Purpose: Retrieve mission details that the current player is authorized to view.

POST `/api/v1/missions/{mission_id}/start`

Purpose: Create or resume an authorized mission run.

GET `/api/v1/mission-runs/{run_id}/next-question`

Purpose: Retrieve the next question in the mission.

POST `/api/v1/mission-runs/{run_id}/answers`

Purpose: Submit an answer and receive validated feedback.

GET `/api/v1/progress`

Purpose: Retrieve the current player's authorized progress.

GET `/api/v1/rewards`

Purpose: Retrieve earned rewards.

Use appropriate HTTP status codes, request validation, structured error responses, authorization, and rate limiting where appropriate.

The actual player authentication and authorization rules must be defined before implementing protected endpoints.

Never trust a player ID supplied by the browser as proof of identity. Determine the authorized player from the authenticated session or an appropriate secure mechanism.

Do not expose answer keys or future mission answers through unrestricted endpoints.

---

# PART 13 — CONTENT CREATION

Prepare an initial bank of at least 100 reviewed questions distributed across the five subjects.

The questions should cover a range of age-appropriate difficulty levels and learning objectives.

Every question should contain:

- Unique identifier.
- Subject.
- Skill or learning objective.
- Age band.
- Difficulty.
- Prompt.
- Answer options where applicable.
- Correct answer.
- Explanation.
- Optional hint.
- Optional image or audio reference.
- Content review status.

Content requirements:

1. Check all answers for accuracy.
2. Ensure explanations are understandable to the target age group.
3. Avoid ambiguous questions.
4. Avoid unnecessarily complex vocabulary.
5. Respect cultural differences.
6. Use properly licensed educational assets.
7. Review generated content before publication.
8. Keep an audit trail for important content changes.

Do not attempt to create hundreds of unreviewed questions before the question engine has been tested.

Start with a small set, verify the full process, and expand to 100 or more reviewed questions during the MVP content milestone.

---

# PART 14 — CHILD SAFETY, PRIVACY, AND ACCESSIBILITY

Child safety is a mandatory product requirement, not a future enhancement.

Implement appropriate protections for the jurisdictions and audiences served.

Requirements:

- Collect the minimum personal information necessary.
- Avoid public direct messaging between children.
- Avoid public disclosure of children's real identities.
- Use age-appropriate nicknames and avatars.
- Do not introduce targeted advertising to children.
- Avoid manipulative purchasing mechanics.
- Protect teacher and guardian functions.
- Provide appropriate guardian controls and consent flows where required.
- Define retention and deletion policies.
- Secure application secrets.
- Protect sessions and authentication.
- Validate all server-side operations.
- Apply reasonable request limits.
- Use HTTPS in production.
- Keep dependencies updated.
- Provide accessible controls and readable content.
- Test the experience with appropriate supervision and permission.

Evaluate applicable child privacy and consumer protection requirements before collecting personal information or launching publicly.

Do not treat a checkbox alone as sufficient parental consent where stronger verification is legally required.

---

# PART 15 — TESTING AND QUALITY ASSURANCE

Use automated tests wherever possible.

## Unit tests

Test:

- Correct and incorrect answers.
- XP calculation.
- Hint-based scoring.
- Completion bonuses.
- Retry behavior.
- Unlock requirements.
- Invalid inputs.
- Difficulty selection.
- Revision scheduling.

## Database tests

Test:

- Player creation.
- Mission creation.
- Attempt persistence.
- Progress persistence.
- Foreign-key integrity.
- Duplicate reward prevention.
- Database migration behavior.

## API tests

Test:

- Valid requests.
- Invalid request data.
- Missing or unauthorized sessions.
- Nonexistent missions.
- Unauthorized progress access.
- Rate limiting.
- Correct response codes.
- Protection against score manipulation.

## Frontend tests

Test:

- Navigation.
- Answer selection.
- Submission.
- Feedback.
- Mission completion.
- Responsive layouts.
- Keyboard navigation.
- Error handling.
- API disconnection.
- Browser refresh and recovery.

## Release acceptance criteria

Do not mark the MVP complete until:

1. The core mission can be played from start to finish.
2. Answers are evaluated correctly.
3. XP is calculated on the server.
4. Rewards cannot be duplicated through ordinary replay or request manipulation.
5. Progress is saved and recovered correctly.
6. All published questions are reviewed.
7. The core interface works on mobile and desktop.
8. Accessibility requirements have been tested.
9. No unresolved critical security defects remain.
10. Appropriate privacy controls and policies are in place.
11. The application has been tested in a staging environment.
12. Backup and recovery procedures have been verified.

---

# PART 16 — DEVELOPMENT ROADMAP

Follow this sequence.

## PHASE 0: Project preparation

Tasks:

- Review this master specification.
- Confirm Python and development tools.
- Create the root folder.
- Create Git repository.
- Establish the initial README.
- Create project status and changelog documents.
- Confirm the folder structure.

Deliverable: a documented, version-controlled project foundation.

## PHASE 1: Python game prototype

Tasks:

- Create the first question bank.
- Implement answer validation.
- Implement scoring.
- Implement feedback.
- Implement mission progression.
- Add five sample missions.
- Add automated unit tests.

Deliverable: a working terminal prototype.

## PHASE 2: FastAPI foundation

Tasks:

- Install and configure FastAPI.
- Build the application entry point.
- Add a health endpoint.
- Add subject and mission endpoints.
- Introduce request and response schemas.
- Test the endpoints.

Deliverable: a functioning Python backend.

## PHASE 3: Database integration

Tasks:

- Configure SQLAlchemy.
- Add initial database models.
- Create database initialization and migrations.
- Add seed data.
- Save mission runs and question attempts.
- Test persistence.

Deliverable: a backend with reliable stored data.

## PHASE 4: Frontend foundation

Tasks:

- Create the HTML entry point.
- Establish CSS design tokens.
- Build the navigation.
- Build the dashboard.
- Build the world map.
- Build the mission screen.
- Connect the frontend to the API.

Deliverable: the first playable browser-based Alpha Quest.

## PHASE 5: Learning and rewards

Tasks:

- Add XP and level progression.
- Add badges.
- Add mission unlocks.
- Add skill progress.
- Add basic adaptive revision.
- Add the Knowledge Builder prototype.

Deliverable: a persistent, motivating educational game.

## PHASE 6: Content and teacher tools

Tasks:

- Expand the reviewed question bank.
- Add teacher authentication.
- Build question-set management.
- Add assignments.
- Add authorized progress reports.

Deliverable: a usable educational platform for supervised classroom and individual learning.

## PHASE 7: Quality assurance

Tasks:

- Run automated tests.
- Test the frontend on different devices.
- Conduct accessibility review.
- Review privacy and security.
- Fix critical bugs.
- Run a controlled pilot.

Deliverable: a stable release candidate.

## PHASE 8: Deployment

Tasks:

- Select suitable hosting.
- Configure production PostgreSQL.
- Set environment variables.
- Configure HTTPS.
- Establish backups and monitoring.
- Deploy a staging version.
- Test the deployment.
- Launch a limited pilot.

Deliverable: an accessible online Alpha Quest pilot.

## PHASE 9: Advanced features

Only after the core MVP is stable:

- Live multiplayer.
- Private classroom game rooms.
- Team Quest.
- More elaborate animation.
- Additional building mechanics.
- More question formats.
- Additional languages.
- Native mobile packaging if justified.
- Optional paid school or teacher features.

---

# PART 17 — PROJECT MANAGEMENT AND DOCUMENTATION

Maintain these documents throughout development:

`README.md`
- Project overview.
- Installation.
- Execution.
- Testing.
- Folder structure.

`docs/master_blueprint.md`
- Approved product specification.

`docs/game_design_document.md`
- Game rules, mechanics, rewards, and progression.

`docs/ui_specification.md`
- Screen designs, components, responsive behavior, and accessibility.

`docs/database_schema.md`
- Tables, relationships, constraints, and migrations.

`docs/test_plan.md`
- Test cases, expected results, and release criteria.

`docs/project_status.md`
- Current phase.
- Completed tasks.
- Active task.
- Known bugs.
- Files created.
- Next steps.

`docs/changelog.md`
- Important changes and reasons.

At the end of every milestone, provide a concise report containing:

1. What was completed.
2. Which files were created or changed.
3. Commands executed.
4. Tests performed and actual results.
5. Known problems.
6. What I learned.
7. The next task.
8. Any changes to the architecture.

Never mark a task complete merely because code was written.

---

# PART 18 — FUTURE BUSINESS MODEL

The initial goal is to produce a useful and engaging game.

Potential future options include:

- Free Explorer experience.
- Teacher Edition.
- School Edition.
- Optional cosmetic customization.
- Additional educational adventure packs.
- Licensed classroom content.
- Institution-level subscriptions.

Do not implement payment processing in the MVP.

Validate educational value and user demand before investing in monetization.

Avoid selling children's personal data or using learning progress to manipulate purchasing decisions.

---

# PART 19 — DEFINITION OF THE MVP

The first public-pilot candidate should include:

- Responsive browser interface.
- Explorer nickname and avatar.
- Five subject worlds.
- A functioning mission system.
- Reviewed questions and explanations.
- XP and reward calculation.
- Saved progress.
- Basic adaptive revision.
- A simple Knowledge Builder.
- Basic progress reporting.
- Automated tests.
- Appropriate privacy and security controls.
- Deployment documentation.

Real-time multiplayer, advanced 3D environments, AI-generated content at runtime, and mobile app store releases are not required for the first MVP.

---

# PART 20 — YOUR FIRST RESPONSE AND FIRST TASK

DeepSeek, read and follow this entire specification.

Do not attempt to generate the whole application in one response.

First, respond with:

1. Your understanding of the Alpha Learning Games and Alpha Quest vision.
2. A concise architecture summary.
3. A review of the proposed technology stack.
4. Any genuine technical risks or inconsistencies in this specification.
5. A list of development phases and their completion criteria.
6. The exact first setup task I should perform.
7. The expected result of that task.
8. The method I should use to report success or an error.

Then begin **PHASE 0, TASK 1**.

Do not skip ahead to Phase 1 until the project foundation is clear.

Give me one manageable task at a time when terminal work or troubleshooting is required. If a task consists of several simple, independent file-creation steps, you may group them together when that will reduce unnecessary repetition.

When providing code, include:

- The exact file path.
- The complete code for the file.
- The terminal command to run it.
- The expected output.
- How to test it.
- Common errors and troubleshooting guidance.

When providing a folder structure, distinguish between planned folders and files that have actually been created.

When a tool or external service is required, explain whether it is free, paid, optional, or necessary. Do not assume that I have a subscription to any service.

If you cannot access my computer, do not claim to have created files on it. Give me the code and commands to run locally.

Preserve the project specification and maintain `docs/project_status.md` as the authoritative progress record.

**The final objective is to build a real, secure, attractive, educational web game that I understand well enough to maintain and improve.**

Begin with PHASE 0, TASK 1. Do not write the entire application at once.
