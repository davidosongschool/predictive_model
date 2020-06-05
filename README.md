# Python predictive model
A predictive model build using python

In the training phase of an experiment, participants were given the 16 training items (see Table 1 below) from which they learned to identify diseases.  									
Participants studied these 16 training items and were assessed to ensure they had learned the disease categories successfully.   									
In the test phase, participants were repeatedly shown 5 test items (see Table 2).  Each time they were shown a given test item, they were asked to rate 									
that item as a member of a different category (category A, category B, and category C) or a different conjunction (conjunctions A&B, A&C, and B&C).									
Participants rated membership on a scale going from -10 (definitely non-member), to 0 (neutral) to +10 (definitely member).									
									
Your task is to come up with a computational model that, for each test item (test items 1 to 5), computes that item's degree of membership in the three categories A, B and C. 									

## Training Data

Table 1.16 training items defined on 3 dimensions Dim1, Dim2, Dim3.Participants learned to identify which items were members of disease category A,	disease categories A and B (conjunction A&B), disease category B, or disease category C.							
Training item number	 Training] item features			Participants learn item is member of disease category or  conjunction			
	Dim 1	Dim 2	Dim 3				
1	A	X	C	category A			
2	A	Y	Y	category A			
3	A	A	X	category A			
4	Y	A	Y	category A			
5	X	A	B	categories A and B			
6	A	B	X	categories A and B			
7	Z	B	B	category B			
8	X	B	B	category B			
9	Y	X	B	category B			
10	Z	Y	B	category B			
11	C	A	Y	category C			
12	C	X	B	category C			
13	C	Y	C	category C			
14	C	A	C	category C			
15	C	X	C	category C			
16	X	Y	C	category C			
