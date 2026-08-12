# Audience Guide

Read this when writing for a specific audience or when one document serves multiple groups.

## What Each Audience Needs

### Engineers
They need exact details. No room for guessing.
- What happens step by step
- Inputs and outputs with real numbers
- What happens when things go wrong
- Code patterns, error messages, state changes
- Leave nothing open to "I think it means..."

### QA
They need to turn your writing into test cases.
- Given [setup], when [action], then [result] — with real values
- Boundary conditions: smallest, largest, zero, negative, null
- Which behavior is required vs. optional
- What error messages should appear

### Sales
They need to talk to customers about this.
- What the customer gets (not how it works inside)
- How to answer "why should I care?"
- How to answer common objections
- Short, memorable talking points they can say in a call

### Customer Support
They need to fix problems fast.
- Step-by-step troubleshooting (if X, do Y)
- Common problems with specific solutions
- When to escalate and to whom
- What to tell the customer at each step

### Executives / Leadership
They need the summary.
- What changed and why, in two paragraphs max
- Impact with numbers if you have them
- What you need from them (decision, approval, awareness)
- Skip the implementation details

### New Team Members
They need the "why" behind everything.
- What this is and why it exists
- What decisions were made and the reasoning
- Definitions of terms insiders use without thinking
- Links to where they can learn more

## The Lowest Common Denominator Rule

When one document serves multiple audiences (like a release note for both sales and support), do not write one version that tries to serve everyone.

Instead, create clearly separated sections — one for each audience. Label them plainly: "For Sales", "For Support."

Each section should feel like it was written specifically for that group. A support person should not have to read the sales section to do their job. A salesperson should not have to wade through troubleshooting steps to find their talking points.
