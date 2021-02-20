# randomize-hashtags
Python script to help generate Random hashtags for Social Media Outreach


## Motivation
Being a photographer, I post and try to maintain a photography profile in Instagram. Now to increase exposure i try to post my pictures with hashtags and using the same set of hashtags doesn't help much. The trick is to jumble / mix match some hashtags in a category. This python script helps to randomly give a sample of hashtags possible around the number limit specified while generating and then you can copy and paste in instgram directly instead of manually choosing and deciding hashtags everytime. Imgaine the pain when one is posting one or more than one pic daily.

## How to Use
* Download the zip and unpack it.
* Install Python 3
* Navigate to the unpacked zip in your terminal
* Run 
```python
	python3 generate.py -cat portraits -no 27
```
* If you want to generate a custom no of hashtags put the number after *-no* flag
* If you want to genarate hashatags under a particular category put the category after *-cat* flag

### How to customise
* If you want to add hashtaggs to the existing category put all hashtags, one in every new line. Note you do not need to worry about duplicates, the generator takes care of picking unique hashtags
* If you want your own set/category, create a category file in .txt extension. For e.g landscape.txt and put all hashtags, one in every new line and while generating put the exact file name after *-cat* flag
