
# Create topic tuple form html file

TOPICS={}

source = 'topic_html.txt'

html_source = open(source, 'r')

text = html_source.read()

current_class = ''

while True:
    topic_index = text.find('req=topicid')
    if topic_index == -1:
        break
    topic_index = topic_index+4
    topic_index_end = text.find('&', topic_index)
    topicid = text[topic_index:topic_index_end]
  
    # get class
    topic_class_index = text.find('class="drop">', topic_index_end)
    topic_class_index_end = text.find('<', topic_class_index)
  
    # get type
    topic_type_index = text.find('column=topic">', topic_index_end)
    topic_type_index_end = text.find('<', topic_type_index)
  
    if topic_class_index < topic_type_index and topic_class_index != -1:
        current_class = text[topic_class_index+13:topic_class_index_end]
        topic_name = current_class
    else:
        current_type = text[topic_type_index+14:topic_type_index_end]
        topic_name = current_class + '/' + current_type
  
    text = text[:topic_index] + text[topic_index_end:]
  
    TOPICS[topic_name] = topicid
  

