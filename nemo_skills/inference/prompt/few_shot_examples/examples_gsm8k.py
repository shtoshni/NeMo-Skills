# Copyright (c) 2024, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Solutions are only in text
only_text = [
    {
        "question": "Missy had a giant piggy bank in her bedroom.  Every day she would search the house for change to put in her bank.  After 4 years, the bank was opened and it contained $450 in change.  If the second, third, and fourth-year she doubled the amount of money she put in the bank from the amount she had put in the previous year, how much money, in dollars, did she put in the bank the first year?",
        "generated_solution": """
Let x be the amount of money Missy put in the bank the first year.
She was then doubling the amount of money every year for 4 years.
So in the second year she put 2*x amount in her bank.
In the third year she put 2*2*x = 4*x amount in her bank.
And in the fourth year she put 2*4*x = 8*x amount in her bank.
So the total amount she put in the bank is x+(2*x)+(4*x)+(8*x)=15*x.
As the problem states, this total amounts to $450.
So 450=15*x which implies x=30.
Thus, Missy put \\boxed{30} dollars in the bank the first year.
""".strip(),
    },
    {
        "question": "Pete has to take a 10-minute walk down to the train station and then board a 1hr 20-minute train to LA. When should he leave if he cannot get to LA later than 0900 hours? (24-hr time)",
        "generated_solution": """
Since Pete needs to take a 10 minutes walk and then a 1 hour 20 minutes train ride, he will spend a total of 1 hour and 30 minutes.
This means that he needs to leave 1 hour and 30 minutes earlier than 09:00 hours.
Subtracting 1 hour and 30 minutes from 0900 hours we get \\boxed{07:30} hours.
""".strip(),
    },
    {
        "question": "Mark deposited $88 in a bank. Bryan deposited $40 less than five times as much as Mark. How much did Bryan deposit in the bank?",
        "generated_solution": """
Five times of what Mark deposited is $88*5=$440.
Bryan deposited $440-$40=$400.
So Bryan deposited \\boxed{400} dollars in the bank.
""".strip(),
    },
    {
        "question": "A department store displays a 20% discount on all fixtures. What will be the new price of a 25 cm high bedside lamp that was worth $120?",
        "generated_solution": """
The lamp was originally priced at $120.
A 20% discount amounts to $120*20/100=$24.
So the discount reduces the price of the lamp to $120-$24=$96.
So the new price of the lamp is \\boxed{96} dollars.
""".strip(),
    },
    {
        "question": "James opens up a flower shop.  He needs to pay rent of $1200 a week with an additional 20% of rent to pay for utilities and he has 2 employees per shift with the store open 16 hours a day for 5 days a week.  If he pays each employee $12.50 an hour, what are his weekly expenses to run the store?",
        "generated_solution": """
The store expense consist of rent, utilities, and employee salaries.
Let's compute each of these expenses separately at a week timescale and then add them up.
The expense due to rent is $1200.
The expense due to utilities is 20% of rent expense. Thus, it is $1200*20/100=$240.
Now we calculate the expense due to employee salaries.
Each employee works 16*5=80 hours per week.
For each employee the cost per week based on hourly wage of $12.5/hr is 12.5*80=$1000 per week.
For two employees, this amounts to 2*$1000=$2000.
Adding the cost of rent, utilities, and employee salaries amounts to $1200+$240+$2000=$3440.
Thus James's weekly expenses to run the store add up to \\boxed{3440} dollars.
""".strip(),
    },
]


only_text_eight_shot = [
    {
        "question": "Missy had a giant piggy bank in her bedroom.  Every day she would search the house for change to put in her bank.  After 4 years, the bank was opened and it contained $450 in change.  If the second, third, and fourth-year she doubled the amount of money she put in the bank from the amount she had put in the previous year, how much money, in dollars, did she put in the bank the first year?",
        "generated_solution": """
Let x be the amount of money Missy put in the bank the first year.
She was then doubling the amount of money every year for 4 years.
So in the second year she put 2*x amount in her bank.
In the third year she put 2*2*x = 4*x amount in her bank.
And in the fourth year she put 2*4*x = 8*x amount in her bank.
So the total amount she put in the bank is x+(2*x)+(4*x)+(8*x)=15*x.
As the problem states, this total amounts to $450.
So 450=15*x which implies x=30.
Thus, Missy put \\boxed{30} dollars in the bank the first year.
""".strip(),
    },
    {
        "question": "Pete has to take a 10-minute walk down to the train station and then board a 1hr 20-minute train to LA. When should he leave if he cannot get to LA later than 0900 hours? (24-hr time)",
        "generated_solution": """
Since Pete needs to take a 10 minutes walk and then a 1 hour 20 minutes train ride, he will spend a total of 1 hour and 30 minutes.
This means that he needs to leave 1 hour and 30 minutes earlier than 09:00 hours.
Subtracting 1 hour and 30 minutes from 0900 hours we get \\boxed{07:30} hours.
""".strip(),
    },
    {
        "question": "Mark deposited $88 in a bank. Bryan deposited $40 less than five times as much as Mark. How much did Bryan deposit in the bank?",
        "generated_solution": """
Five times of what Mark deposited is $88*5=$440.
Bryan deposited $440-$40=$400.
So Bryan deposited \\boxed{400} dollars in the bank.
""".strip(),
    },
    {
        "question": "A department store displays a 20% discount on all fixtures. What will be the new price of a 25 cm high bedside lamp that was worth $120?",
        "generated_solution": """
The lamp was originally priced at $120.
A 20% discount amounts to $120*20/100=$24.
So the discount reduces the price of the lamp to $120-$24=$96.
So the new price of the lamp is \\boxed{96} dollars.
""".strip(),
    },
    {
        "question": "James opens up a flower shop.  He needs to pay rent of $1200 a week with an additional 20% of rent to pay for utilities and he has 2 employees per shift with the store open 16 hours a day for 5 days a week.  If he pays each employee $12.50 an hour, what are his weekly expenses to run the store?",
        "generated_solution": """
The store expense consist of rent, utilities, and employee salaries.
Let's compute each of these expenses separately at a week timescale and then add them up.
The expense due to rent is $1200.
The expense due to utilities is 20% of rent expense. Thus, it is $1200*20/100=$240.
Now we calculate the expense due to employee salaries.
Each employee works 16*5=80 hours per week.
For each employee the cost per week based on hourly wage of $12.5/hr is 12.5*80=$1000 per week.
For two employees, this amounts to 2*$1000=$2000.
Adding the cost of rent, utilities, and employee salaries amounts to $1200+$240+$2000=$3440.
Thus James's weekly expenses to run the store add up to \\boxed{3440} dollars.
""".strip(),
    },

    {
        "question": 'Yvonne brings a box of chocolates to school. Half have nuts and half do not. The students eat 80% of the ones with nuts and eat half of the ones without nuts. If there are 28 chocolates left, how many chocolates were in the box?',
        "generated_solution": """
The ones with nuts that they ate was 40% of the box because 80% x .5 = 40%. 
The ones without nuts that they ate equaled 25% of the box because 50% x .5 = 25%. 
They ate 65% of the box because 40 + 25 = 65. 
They left 35% of the box because 100 - 65 = 35. 
The box had 80 chocolates because 28 / .35 = 80. 
Thus, the box originally had \\boxed{80} chocolates.
""".strip(),
    },
    {
        "question": 'In five years, Grant will be 2/3 the age of the hospital that he is hired into. If Grant is currently 25 years old, how old is the hospital now?',
        "generated_solution": """
If Grant is currently 25 years old, he will be 25+5 = 30 years old in five years. 
If 2/3 of hospital's age in five years represents Grant's age in five years, then the hospital's age in five years would be 30/(2/3) = 45 years. 
So, the hospital is currently 45-5 = 40 years old. 
Thus, the hospital is \\boxed{40} years old.
""".strip()
    },

    {
        "question": "Very early this morning, Elise left home in a cab headed for the hospital. Fortunately, the roads were clear, and the cab company only charged her a base price of $3, and $4 for every mile she traveled. If Elise paid a total of $23, how far is the hospital from her house?",
        "generated_solution": """
For the distance she traveled, Elise paid 23 - 3 = 20 dollars. 
Since the cost per mile is $4, the distance from Elise's house to the hospital is 20/4 = 5 miles.
Thus, the hospital is \\boxed{5} miles away from Elises's house.""",
    },
]

generate_masked = [
    {
        "question": "Missy had a giant piggy bank in her bedroom.  Every day she would search the house for change to put in her bank.  After 4 years, the bank was opened and it contained $450 in change.  If the second, third, and fourth-year she doubled the amount of money she put in the bank from the amount she had put in the previous year, how much money, in dollars, did she put in the bank the first year?",
        "reference_solution": "We let x be the amount of money she put in the bank the first year.\nThen the second year was 2*x, \nand the third year was 2*2*x=4*x,\nand the fourth year was 2*2*2*x=8*x.\nAnd the total amount she put in the bank, $450, is the sum of all four years, or $450 = x+(2*x)+(4*x)+(8*x).\nThis simplifies to $450=15*x.\nAnd therefore, the amount of money she put in the bank the first year was x=$30.",
        "generated_solution": """
We let x be the amount of money she put in the bank the first year.\nThen the second year was 2*x, \nand the third year was 2*2*x=M*x,\nand the fourth year was 2*2*2*x=N*x.\nAnd the total amount she put in the bank, $450, is the sum of all four years, or $450 = x+(2*x)+(M*x)+(N*x).\nThis simplifies to $450=(1 + 2 + M + N)*x.\nAnd therefore, the amount of money she put in the bank the first year was x=P dollars.
""".strip(),
    },
    {
        "question": "Pete has to take a 10-minute walk down to the train station and then board a 1hr 20-minute train to LA. When should he leave if he cannot get to LA later than 0900 hours? (24-hr time)",
        "reference_solution": "There are 60 minutes in an hour so 1 hour 20 minutes = (60+20) minutes = 80 minutes\nHe will spend a total of 80+10 = 90 minutes\n90 minutes is = (60/60) hours and 30 minutes = 1 hour 30 minutes = 0130 in 24-hr time\nHe has to leave 0130 hours earlier than 0900 i.e. 0900-0130 = 0730 hours",
        "generated_solution": """
There are 60 minutes in an hour so 1 hour 20 minutes = M minutes\nHe will spend a total of M + 10 = N minutes\nN minutes is = O hours and P minutes = O hour P minutes = Q in 24-hr time\nHe has to leave Q hours earlier than 0900 i.e. 0900 - Q = R hours""".strip(),
    },
    {
        "question": "Mark deposited $88 in a bank. Bryan deposited $40 less than five times as much as Mark. How much did Bryan deposit in the bank?",
        "reference_solution": "Five times the amount Mark deposited is $88 x 5 = $440.\nSo, Bryan deposited $440 - $40 = $400.",
        "generated_solution": """
Five times the amount Mark deposited is $88 x 5 = M.\nSo, Bryan deposited M - $40 = N.""".strip(),
    },
    {
        "question": "A department store displays a 20% discount on all fixtures. What will be the new price of a 25 cm high bedside lamp that was worth $120?",
        "reference_solution": "The amount of the discount is $120 x 0.2 = $24.\nThe new price will be $120 \u2013 $24 = $96.",
        "generated_solution": """
The amount of the discount is $120 x 0.2 = M.\nThe new price will be $120 \u2013 M = N.
""".strip(),
    },
    {
        "question": "James opens up a flower shop.  He needs to pay rent of $1200 a week with an additional 20% of rent to pay for utilities and he has 2 employees per shift with the store open 16 hours a day for 5 days a week.  If he pays each employee $12.50 an hour, what are his weekly expenses to run the store?",
        "reference_solution": "He is open 16*5=80 hours a week.\nSo he pays each of his employees 12.5*80=$1000 per week.\nSince there are two employees, he pays them in total 2 * $1000 = $2000 per week.\nThe utilities cost 1200*.2=$240.\nSo his total cost per week is 1200+2000+240=$3440",
        "generated_solution": """
He is open 16 * 5 = M hours a week.\nSo he pays each of his employees 12.5 * M = N per week.\nSince there are two employees, he pays them in total 2 * N = O per week.\nThe utilities cost 1200 * .2 = P.\nSo his total cost per week is 1200 + O + P = Q
""".strip(),
    },
]


examples_map = {
    "gsm8k_generate_masked": generate_masked,
    "gsm8k_only_text": only_text,
    "gsm8k_eight_shot": only_text_eight_shot,
}


if __name__ == '__main__':
    print(only_text[4]["generated_solution"])