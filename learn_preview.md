# Preview of the LMS

## The Learn Platform

- Learn is an learning management system (LMS). It specializes in supporting programming curriculum.

  - Has a lot of autograding capabilities
  - Tracks student progress well
  - Pushes Ada to form curriculum towards "visible forward progress" with clear feedback about what work has been done and what work remains

- Students will approach a **topic** which contains many **lessons**
  - For example, there is a **topic** "Intro to Tests"
  - This topic contains the following **lessons**:
    - Packages and Managing Packages
    - Automated Tests
    - Intro to pytest
    - Practice: Intro to pytest

![Screenshot of Learn: Main Ada Core page with multiple topics](assets/learn_preview_1_splash.png)

- Learn supports a bunch of different autograded questions, such as:
  - Multiple choice
  - Reordering
  - Code challenges

![Screenshot of Learn: A multiple choice question](assets/learn_preview_2_mc.png)

![Screenshot of Learn: An ordering question](assets/learn_preview_3_order.png)

- Code challenges will pass or fail based on provided tests
- The tests are technically written in unittest, not pytest. In my opinion, they're comparable/both readable
- Students can submit an infinite number of times
- Most/all code challenges will provide an example solution

![Screenshot of Learn: Code challenge initial appearance](assets/learn_preview_4_cc_initial.png)

![Screenshot of Learn: Code challenge with failure and test failure detail](assets/learn_preview_5_cc_failure.png)

![Screenshot of Learn: Code challenge with success and explanation](assets/learn_preview_6_cc_success.png)

- For the curious about the backend, Learn lets us look at student stats (how many challenges they get correct), and their progress (how many topics and lessons have they read and completed?)
- We get a lot of detail! We can see their submissions per question

![Screenshot of Learn: Student statistics view](assets/learn_preview_7_stats.png)

![Screenshot of Learn: Student progress view](assets/learn_preview_8_progress.png)

![Screenshot of Learn: Student progress view with question details expanded](assets/learn_preview_9_progress_expanded.png)
