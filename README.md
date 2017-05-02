# javaranch-data
Cleaning up and formatting java questions from the [java ranch roundup game](http://www.javaranch.com/roundup.jsp). Want to use the data? Look [here](http://seanastephens.github.io/javaranch-data/questions.json) for v1 and [here](http://seanastephens.github.io/javaranch-data/questions.v2.json) for v2.

Forked from [https://github.com/seanastephens/javaranch-data](https://github.com/seanastephens/javaranch-data), modified for CSc 335 Spring 17.

# JSON Layout

    [
      {
       "id": "1",
       "line": "A string question related to some detail of java",
       "answer": "A string answer to the line element question",
       "explanation": "A string explanation as to why the answer is correct",
       "bogus": [
          "An array of incorrect string answers"
        ]
      }
    ]

# V2 JSON Layout

    [
      {
       "id": "1",
       "question": "A string question related to some detail of java",
       "answers": [
          {
           "answer": "A string multiple choice answer to the question",
           "correct": "truthy value if this is the correct answer"
          }
        ]
       "explanation": "A string explanation as to why the answer is correct",
      }
    ]
