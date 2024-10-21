
def answePrompt(data):
    getAnswer = f"""
        You are a financial expert. You are supposed to answer the given question. 
        Here is the question:
        Share context: {data.get('Share Context')}

        Question: {data.get('Question Text')}

        Options: {data.get('Options')}

        First, think through the problem step by step, documenting each necessary step clearly. 
        Ensure that all math symbols, equations, and formulas in the reasoning steps are enclosed in double dollar signs ($$ $$) for LaTeX rendering. 
        Each formula should be wrapped in $$, like this: $$ your_formula $$. Ensure every formula follows this structure without exception.
        Finally, conclude your response with the final answer in your last sentence as “Therefore, the answer is \\boxed{{}}”.
        Only one letter like "A" or "B" or "C" or "D" is allowed in the \\boxed{{}} (e.g., \\boxed{{A}}).
        """
    return getAnswer

def feedbackPrompt(data,modelAnswer, modelReasoning):
    feedback = f"""
        You are a financial expert. You are supposed to provide feedback on the given info, including question info, crrorect answer and reasoning \n
        step and wrong answer and reasoning step. 
        Here is the question:
        Share context: {data.get('Share Context')}
        Question: {data.get('Question Text')}
        Options: {data.get('Options')}

        Here is the correct answer and reasoning step:
        Correct Reasoning step: {'Correct Reasoning step: '+ data.get('Explanation')}
        Correct Answer: {'Correct Answer: '+ data.get('Answer')}

        Here is the model's wrong answer and wong reasoning step:
        Wrong Reasoning step: {'Wrong Reasoning step:'+ modelReasoning}
        Wrong Answer: {'Wrong Answer: '+ modelAnswer}
        
        the feedback should be in the content:
        1. rewrite correct reasoning step.
        2. compare the correct reasoning step with the model's wrong reasoning step, and point out the difference.
        3. summarize the hint for future simalar questions.

        Ensure that all math symbols, equations, and formulas in the feedback are enclosed in double dollar signs ($$ $$) for LaTeX rendering. 
        Each formula should be wrapped in $$, like this: $$ your_formula $$. Ensure every formula follows this structure without exception.

        Here is the example:
            "Feedback":{
                "corrected_reasoning_steps": 
                    [
                        "### Correct Reasoning" ,
                        "the rewrite correct reasoning step"
                        "### Final Answer",
                        "Therefore, the answer is \\boxed{A}."
                    ],

                "comparison": 
                    [
                        "incorrect_reasoning": "Initially, the reasoning focused on finding the best portfolio in terms of risk-return trade-off, leading to Portfolio 2 being chosen as the best option. However, the question was asking for the least efficient portfolio, not the best one.",
                        "correct_reasoning": "The correct reasoning focuses on identifying the portfolio that is not mean-variance efficient. Portfolio 1 is suboptimal because it has both a lower return and higher risk than Portfolios 2 and 3, making it inefficient.",
                        "main_difference": "The key difference was misunderstanding the question's focus—choosing the least efficient portfolio rather than the best one."
                    ],

                "keyTakeaways": 
                    [
                        "1. Always read the question carefully to understand whether it is asking for the most efficient or the least efficient portfolio." ,
                        "2. Apply the concept of mean-variance efficiency by comparing portfolios to identify suboptimal ones.",
                        "3. Look for portfolios that have both higher risk and lower return compared to others to determine inefficiency.",
                        "4. Be mindful of dominance when comparing portfolios—if one portfolio offers both a higher return and lower risk, the other is not efficient."
                    ]
        }
        """
    return feedback


def ICLPrompt(error_log,data):
    ICL_Prompt=f"""
    You are a financial expert. You are supposed to answer the given question before you do in-conext learning according to additional samilar question's Feedback.
    Here is the similar question and feedback:
    Share context: {error_log.get('Share Context')}
    Question: {error_log.get('Question Text')}
    Options: {error_log.get('Options')}
    Feedback: {error_log.get('Feedback')}

    Here is the question:
    Share context: {data.get('Share Context')}
    Question: {data.get('Question Text')}
    Options: {data.get('Options')}

    Learn the similar question and its feedback and then answer the question.
    First, think through the problem step by step, documenting each necessary step clearly. 
    Ensure that all math symbols, equations, and formulas in the reasoning steps are enclosed in double dollar signs ($$ $$) for LaTeX rendering. 
    Each formula should be wrapped in $$, like this: $$ your_formula $$. Ensure every formula follows this structure without exception.
    Finally, conclude your response with the final answer in your last sentence as “Therefore, the answer is \\boxed{{}}”.
    Only one letter like "A" or "B" or "C" or "D" is allowed in the \\boxed{{}} (e.g., \\boxed{{A}}).
    """
    return ICL_Prompt