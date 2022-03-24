# 1. Data
# Import packages
import wikipedia
import re

# Specify the title of the Wikipedia page
# 한글 위치 사용
# wikipedia.set_lang('ko')
# wiki = wikipedia.page("학교")

wiki = wikipedia.page("COVID-19")
# Extract the plain text content of the page
text = wiki.content
# Clean text
text = re.sub(r'==.*?==+', '', text)
text = text.replace('\n', '')


# 2. WordCloud
# Import package
import matplotlib.pyplot as plt
# Define a function to plot word cloud
def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud) 
    # No axis details
    plt.axis("off");
    plt.show()


# Import package
from wordcloud import WordCloud, STOPWORDS
# Generate word cloud
font = "C:\\Windows\\Fonts\\malgun.ttf"

wordcloud = WordCloud(font_path=font, width= 3000, height = 2000, random_state=1, background_color='salmon', colormap='Pastel1', collocations=False, stopwords = STOPWORDS).generate(text)
# Plot
plot_cloud(wordcloud)

# Ref: https://towardsdatascience.com/simple-wordcloud-in-python-2ae54a9f58e5
# Mask Img Ref: https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=kisma&logNo=221645672632