# Deliverable Structure

Use this structure for long teardowns and explainer pages unless the user asks for a different format.

## 1. Start with one scene

Open with a real action the reader can picture:
- a customer pays
- a creator uploads a video
- a team connects a social account
- a user asks the AI for an answer

This is the anchor scene for the rest of the explanation.

## 2. Explain the product job

Answer:
- what problem the product solves
- who it is for
- what result it promises

Keep this short. The goal is to orient the reader, not to restate the marketing copy.

## 3. Show the architecture as layers

Use a clear layer order:
- user and interface layer
- application logic layer
- data and infrastructure layer
- third-party services layer

If there are workers, queues, or AI pipelines, show them as supporting lanes with visible arrows.

## 4. Show how messages move

Explain communication like message passing:
- user tells the app something
- the app asks a service for help
- the service sends a status update back
- the database records the result

For billing and auth flows, make event handoffs explicit.

## 5. Translate the important technologies

Only mention technologies that matter to:
- the user experience
- the business model
- the operational cost
- the product's differentiation

Do not dump a dependency list without context.

## 6. Add the SaaS toolbox

For each third-party service, include:
- what it does
- what part of the stack it belongs to
- which other services or app modules depend on it
- the free tier
- the paid pricing
- the common trigger for upgrading

## 7. Close with tradeoffs

Summarize:
- what this architecture is good at
- where it gets expensive
- where it gets fragile
- what a smaller team might simplify
