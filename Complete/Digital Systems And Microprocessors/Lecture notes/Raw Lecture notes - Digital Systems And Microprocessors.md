# First lecture
2024-01-30 @ 11:58 
Digital signals are not necessarily [[Binary]] they can have a number of levels as long as they are a discrete number of levels that can be represented by a bit stream.
### Working
$f(w,x,y,z) = \sum()$
![[K-map Example]]

$f(w,x,y,z) = \sum()$

$f = AB+CD$

![[Logical diagrams working out]]
![[K-map Example 1]]
### Installing Vivado
2024-01-30 @ 17:34 
https://www.xilinx.com/support/download.html
`sudo Downloads/FPGAs_AdaptiveSoCs_Unified_2023.2_1013_2256_Lin64.bin`
installed the full vivado suite standard edition
! Cable Drivers not available on Linux need to install following instruction from UG973
### FPGA vs Microprocessor
2024-01-30 @ 18:02 
#definition FPGA stands for Field Programable Gate Array which is a bit like a tiny bread board of logical gates that you can connect to your liking. low level customisation can allow for a more ergonomic solution However FPGA's can use more power & cost more than an equivalent microprocessor. 

## Assignment
### Pre-requisites:
1. Install Verilog
2. Learn basic Verilog Programming
3. Understand how to use and program in Vivado Design Suite (from Xilinx)
4. Learn how to create a test bench (You can write one in Verilog or else Vivado can create one for your design)
### Q1. 
Write Verilog programs for the following Boolean logic gates and also simulate them by creating test-bench for all possible input combinations. The test bench should be able to test the output for all possible input combinations. (5 marks)
- (a) 2-input AND gate
- (b) 3-input OR gate
- (c) 2-input NAND gate
- (d) 2-input NOR gate
- (e) 2-input XOR gate
### Q2. 
For the Boolean logic expression: (5 marks)
	F = A’BC’ + AB’C’ + ABC’a. 
1. Write a Verilog program which implements the above Boolean expression, and write a test-bench to simulate it.
2. Reduce the same expression using K-map and then write a Verilog code for the reduced expression. Write the test-bench and simulate the reduced expression.

You do not need to submit a report for this assignment. However, in the final graded assignment youwill be expected to provide
1. The Verilog codes to all assignment questions and test benches
2. Screenshots of all outputs (logic design layout and simulations)

### NEXT WEEK:
1. Learn about different data types: “wires”, “nets”, “registers” and “parameters”. You will needto implement.
2. Read the Verilog Programming and FPGA documents available on blackboard

# Week 2
2024-02-06 @ 16:51 
### Adders
#### Full adder


to represent a negative number you take its second complement
#definition to take the compliment of a binary number you flip every bit (eg: $0010 \to 1101$) and then the second compliment is this +1 (eg: $0010^{c_2} = 1110$)
### Subtracting in Binary
To do the following denary subtraction, $120 - 85 = 35$, in binary
Where:
	$120 = 1111000$
	$85 = 1010101$
the second compliment is taken of `1010101` in order to represent $-85$ and then the values are added.
$$\begin{align}
&1111000 + 1010101^{c_{2}} \\
&1111000 + (0101010+1) \\
&1111000 + 0101011 \\
= &10100011
\end{align}$$

## Assignment
2024-02-12 @ 17:42 
### Q1
- [x] (a) First create modules for AND and XOR gates using behavioral modeling scheme ✅ 2024-02-12
	https://technobyte.org/verilog-exor-gate/#Verilog_code_for_XOR_gate_using_behavioral_modeling
- [x] (b) Use these modules to implement a Half-Adder using structural modeling ✅ 2024-02-12
(c) Using the Half-Adder design and OR gate module, implement a Full-Adder design using structural modelling. Write a testbench and simulate your Full Adder design.

### Q2
Using the Full-Adder design in Ques 1(c), construct a 4-bit ripple carry adder using structural modeling. Write a testbench to simulate your design.
### Q3
Using Gate-Level primitives implement a Full-Subtractor design. Simulate and test your design using testbench.
### Q4 
Design a 4-bit Adder-Subtractor module using structural modelling. Simulate your design using testbench.

# Week 3
2024-02-13 @ 16:59 
## Tutorial questions
2024-02-13 @ 16:59 
[[Tutorial - Combinational logic circuits - without animation.pdf]]
### Example 1
#### A)
t1 = b' AND c
t2 = a' AND b
t3 = a OR b 
t4 = (a' & b) XOR D

F1 = (a OR b) OR ((a' & b) XOR D)
F2 = (a' AND b) OR d'
#### B)

#### C)

### Example 4
a
	01101
b
	11001
c

### Example 5
2024-02-13 @ 17:05 
#### Truth table
| x | y | z |  | a | b | c |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|  |  |  |  |  |  | 1 |
|  |  | 1 |  |  | 1 |  |
|  | 1 |  |  |  | 1 | 1 |
|  | 1 | 1 |  | 1 |  |  |
| 1 |  |  |  |  | 1 |  |
| 1 |  | 1 |  |  | 1 | 1 |
| 1 | 1 |  |  | 1 |  |  |
| 1 | 1 | 1 |  | 1 |  | 1 |
#### K maps
##### A
| x\yz | 00 | 01 | 11 | 10 |
| ---- | ---- | ---- | ---- | ---- |
| 0 |  |  | 1 |  |
| 1 |  |  | 1 | 1 |
##### B
| x\yz | 00 | 01 | 11 | 10 |
| ---- | ---- | ---- | ---- | ---- |
| 0 |  | 1 |  | 1 |
| 1 | 1 | 1 |  |  |
##### C
| x\yz | 00 | 01 | 11 | 10 |
| ---- | ---- | ---- | ---- | ---- |
| 0 | 1 |  |  | 1 |
| 1 |  | 1 | 1 |  |
## Assignment
Read about structural modelling and perform the following tasks:
### 1.
Using gate level primitives, build a three-to-eight line decoder module with an enablepin. (4 marks)
### 2. 
Using structural modeling, using the the 3-to-8 line decoder module above to build a 4-to-16 line decoder module. (2 marks)
### 3. 
Use structural modeling to construct a full adder module using 3-to-8 line decodermodule above and OR gates. (4 marks)

Study dataflow modeling and behavioral modeling (from the book, chapter 4). Read aboutwhen to use “always” and when to use “assign” and then perform the following tasks:
### 4. 
Construct a 2-to-1 line multiplexer module using dataflow modeling. (2 marks)
### 5. 
Then use three 2-to-1 line multiplexer modules to construct a 4-to-1 line multiplexermodule using structural modeling. (4 marks)
### 6. 
Construct a 4-to-1 line multiplexer using behavioral modeling. (4 marks)

# Week 4
2024-02-20 @ 15:50 
#definition **Sequential** logic circuits output are a function of present & past inputs.
#definition **Synchronous** logic circuits are a type of sequential logic circuit where the feedback signal is regulated by a clock pulse.


## Assignment
### Q1. 
You have to design a lawn sprinkler controller. The controller can accept three inputs: 
1. START
2. DRYNESS
3. RAIN
It produces two outputs:
1. SPRINKLER_ON
2. WATER_FLOW
The description of input/output signals is as follows: 
- START = 1. Start sprinkler in the morning (ON=1), if and only if it is needed.
- DRYNESS: is a 2-bit input: 
	- 00 = too dry, 
	- 01 = dry, 
	- 10 = wet, and 
	- 11 = fully watered.
- RAIN = 1. It is raining then the sprinkler should not be turned on.
- SPRINKLER_ON = 1. Turn on the sprinkler system.
- WATER_FLOW is a 2-bit output which controls the flow of water: 
	- 11 = maximum flow, 
	- 10 =medium flow, 
	- 01 = drip, and 
	- 00 = no flow.
The sprinkler system is turned on (set ON=1), if START =1. The lawn is not fully watered and it is not raining. The output flow should be “maximum” when the lawn is too dry, “medium when it is dry, and “drip” when it is wet. The sprinkler should be turned off when the lawn is fully watered.

#### a. Show all design steps to arrive at the combinational logic circuit.
##### Truth table
| START | RAIN | DRYNESS 1 | DRYNESS 2 | SPRINKLER_ON | WATER_FLOW 1 | WATER_FLOW 2 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 0 | 0 | 0 | 0 | 0 | na | na |
| 0 | 0 | 0 | 1 | 0 | na | na |
| 0 | 0 | 1 | 0 | 0 | na | na |
| 0 | 0 | 1 | 1 | 0 | na | na |
| 0 | 1 | 0 | 0 | 0 | na | na |
| 0 | 1 | 0 | 1 | 0 | na | na |
| 0 | 1 | 1 | 0 | 0 | na | na |
| 0 | 1 | 1 | 1 | 0 | na | na |
| 1 | 0 | 0 | 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 | 0 | na | na |
| 1 | 1 | 0 | 1 | 0 | na | na |
| 1 | 1 | 1 | 0 | 0 | na | na |
| 1 | 1 | 1 | 1 | 0 | na | na |

`SPRINKLER_ON = START && ~RAIN && ~(DRYNESS 1 && DRYNESS 2)`

`WATER_FLOW = ~ DRYNESS`
	`WATER_FLOW 1 = ~ DRYNESS 1`
	`WATER_FLOW 2 = ~ DRYNESS 2`

#### b. Show the final logic diagram that you are implementing


#### c. Design this controller using Verilog. Write a test bench to and simulate the design.


### Q2. 
Design a **4-bit Adder-Subtractor** module using structural modelling. (10 marks)
a. First design a single bit full adder circuit and then use structural modelling to create a 4-bitadder-subtractor unit.
b. Simulate your design using testbench.

While attempting the questions consider the following steps:
- Go over all solution steps and logic diagrams (to show what you are implementing)
- Verilog codes with good remark statements and proper variables (for inputs and outputs). 
- Also write thetest bench to test all possible input scenarioso Check the behavioral Block Diagram (extracted from Vivado)
- Finally, critically analyze your results and discuss them with your fellow students. See if they used a different(more efficient) way to get the same answers).