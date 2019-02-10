
# coding: utf-8

# In[ ]:


#STEP 1


# In[ ]:


#NASA MARS NEWS


# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time


# In[2]:

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)


# In[3]:
def scrape():
    listings = {}
    browser = init_browser()
    
    


# In[5]:


    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(2)


    # In[7]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[8]:


    results = soup.find_all('li', class_="slide")
    #print(results)


    # In[9]:


    for result in results:
        title = result.find('div', class_="content_title")
        news_title = title.a.text
        title_p = result.find('div', class_="article_teaser_body")
        news_title_p = title_p.text
        break
    print(news_title)
    print(news_title_p)


    # In[10]:


    listings["news_title"]=news_title
    listings["news_title_p"]=news_title_p


    # In[11]:


    #JPL MARS SPACE IMAGE - FEATURED IMAGE


    # In[12]:


    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars/"
    browser.visit(url)


    # In[13]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[14]:


    results = soup.find_all('div', class_="carousel_items")
    #print(results)


    # In[15]:


    for result in results:
        link = result.find('a')
        url = link["data-fancybox-href"]
        featured_image_url = 'https://www.jpl.nasa.gov' + url
        featured_image_url= featured_image_url.replace('mediumsize','largesize')
        featured_image_url= featured_image_url.replace('ip','hires')


    # In[16]:


    listings["featured_image_url"]=featured_image_url


    # In[17]:


    #MARS WEATHER


    # In[18]:


    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)


    # In[19]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[20]:


    results = soup.find_all("li", class_="js-stream-item")
    #print(results)


    # In[21]:


    tweets=[]

    for result in results:
        container = result.find('p')
        tweets.append(container)
    #print(tweets[0])


    # In[22]:


    mars_weather = tweets[0].text


    # In[23]:


    listings['mars_weather'] = mars_weather


    # In[24]:


    #Mars Facts


    # In[25]:


    url = "https://space-facts.com/mars/"
    browser.visit(url)


    # In[26]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[27]:


    tables = pd.read_html(url)
    tables


    # In[28]:


    df = tables[0]


    # In[29]:


    df = df.rename(index=str, columns={0: "description", 1: "measurements"})


    # In[30]:


    df


    # In[31]:


    html_table = df.to_html(index=False)
    listings['html_table']=html_table


    # In[32]:


    #Mars Hemisphere


    # In[33]:


    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[34]:


    results = soup.find_all('div', class_="item")
    #print(results)
    #results


    # In[35]:


    name=[]
    img_url = []


    for result in results:
        hemi = result.find('h3').text
        name.append(hemi)
        
        pic = result.find("a")
        link = pic['href']
        url1 = link[24:]
        url2 = "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/" + url1 + ".tif/full.jpg"
        img_url.append(url2)
        #link.lstrip('/search/map/Mars/Viking/')


    # In[36]:


    name


    # In[37]:


    img_url


    # In[38]:


    hemisphere_image_urls = [
        {"title": name[0], "img_url": img_url[0]},
        {"title": name[1], "img_url": img_url[1]},
        {"title": name[2], "img_url": img_url[2]},
        {"title": name[3], "img_url": img_url[3]},
    ]


    # In[39]:


    listings['hemisphere_image_urls']=hemisphere_image_urls


    # In[41]:


    return listings
        
