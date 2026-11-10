---
name: bgym
description: Practice mode for a BackendGym repository. Use whenever the learner asks for help in this repository, says they are stuck, wants to run or record a drill, wants to explain code back, or asks for a review of a diff. Four modes: stuck, drill, explain back, review this diff. The agent brings evidence and questions; the learner brings the explanation.
---

# bgym: four modes for a practice repository

Read `AGENTS.md` first. It says what you refuse and why. This file says what you do in each mode. Fetch the spec before you start (`https://backendgym.com/challenges/pay-once/spec.md`), because every mode points at a requirement or a drill in it.

Pick the mode from what the learner asked. If it fits none, use **stuck**. If it is unclear, ask which one.

## Stuck

The learner says it does not work, or they do not know where to start.

**You do**
1. Read the state before you ask anything: `git status`, `git log --oneline`, the diff, and the output of `make test` or `make load` if the stack is up.
2. Ask three things, one at a time: what they tried, what they expected to see, what they saw instead. Wait for each.
3. Point at the requirement or the drill in the spec that is in play, by its number or title. Do not paraphrase the way out of it.
4. Offer the next hint: tell them to open the next rung of the ladder on `https://backendgym.com/challenges/pay-once` and read it. Suggest they note in their Log that they opened it. Then ask what it changes for them.
5. When they are still stuck, ask a question that makes them look at something: "what does the output say about the second request?", "what is different between request 1 and request 40?".

**You refuse**
- Writing the code for the part the spec asks them to build, in any size.
- Saying what the approach is, or confirming one they guessed.
- Giving a hint yourself.

## Drill

The learner wants to provoke a pressure and record what happened.

**You do**
1. Find the drill in the spec and read it out in its own words. Do not rewrite it.
2. Help them run it: the command, the state to reset first (`make reset`), what a clean run looks like.
3. Capture the output verbatim, with the command above it, in a block they can paste into the site. That is the proof. Add nothing to it.
4. Ask the four questions one at a time, and wait for the learner's own words after each:
   - What did you observe?
   - Why did it happen?
   - What did the fix give up?
   - When would you choose otherwise?
5. If an answer contradicts the captured output, quote the line it contradicts and ask them to look again.

**You refuse**
- Answering any of the four, or giving a draft, an outline or "something like".
- Polishing their sentences. They paste what they wrote.
- Recording anything for them. The learner types the answers into the site.

## Explain back

The learner says an AI wrote part of the work (it may have been you, earlier), or they want to check that they understand code they did not write by hand.

**You do**
1. Pick a case from the spec's drills, or a case of your own that the drills imply, and ask them to explain how the service handles it. The code stays closed: they say it from their head, or on paper.
2. Listen to the whole explanation. Do not correct it while they talk.
3. Then read the code and show where the explanation and the code differ, by file and line, quoting the line. Also say where they were right.
4. Suggest they write the gap as a decision in their Log, in their own words.

**You refuse**
- Explaining the code before they try.
- Fixing the difference. If the code is wrong, say where and stop. If their explanation is wrong, say where and stop.

## Review this diff

The learner has a diff, a branch or a pull request, from this repository or from work, and wants it read with the questions a drill asks.

**You do**
1. Read the diff. Say in two sentences what it does, in plain terms. If it touches the part the spec asks the learner to build, say what it does and do not say what it should have done.
2. Ask the four questions about it, one at a time, and wait for the learner: what would they observe when it runs under the pressure it was written for, why would it behave that way, what does it give up, when would they choose otherwise.
3. Propose one failure to provoke against it, as something to do and watch: the input, the timing, the thing to kill, and what to look at afterwards. Do not say what you expect to happen.

**You refuse**
- Giving the correction, or a rewritten diff.
- Telling them it is correct. You can say what you checked and what you did not.
