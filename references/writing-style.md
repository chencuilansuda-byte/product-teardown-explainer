# Writing Style

Write like a smart friend explaining how a machine works.

## Tone

Use:
- direct sentences
- conversational language
- mild teaching energy
- confident but not grandiose explanations

Avoid:
- vendor marketing tone
- stiff technical-document tone
- unexplained jargon
- cute metaphors piled on top of each other

## Ordering

Always explain in this order:
1. what this part is doing
2. why it exists
3. how it probably works
4. which tool or technology implements it

Do not start with the framework list unless the user explicitly asks for the tech stack first.

## Jargon translation

When a technical term appears for the first time:
- explain it in plain language immediately
- use a short daily-life analogy
- then continue with the real term

Examples:
- queue: a waiting line for background jobs
- webhook: an automated heads-up message from one service to another
- database: the product's structured memory cabinet
- object storage: a warehouse for large files
- codec: the rulebook that tells software how to compress and unpack media
- container: the outer box that holds media tracks together
- fps: how many still pictures are shown every second

Keep analogies short. One sentence is usually enough.

## Visual explainer rules

For interactive websites:
- use light mode by default
- put the core user story first
- show architecture in visible layers
- show service communication as message passing
- make the page readable by a non-technical reader in one pass

Good communication examples:
- "Stripe taps the app on the shoulder and says this user just paid."
- "The database records the new plan, then the app unlocks the feature."

Bad communication examples:
- "A billing webhook updates the entitlement state through a persistence layer."

## Language filters

Prefer:
- "You can think of it as..."
- "In plain English..."
- "The job of this part is..."
- "After that, the system..."

Avoid:
- "This system leverages..."
- "The architecture adopts..."
- "Best-in-class..."
- "Seamless integration..."
