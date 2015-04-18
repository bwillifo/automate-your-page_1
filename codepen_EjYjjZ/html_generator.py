def generate_concept_HTML(concept_title, concept_description, concept_subtitle, concept_body):
    html_text_1 = '''
<div class="lesson">
    <h2 id="'''+ concept_title + '"' + ">" + concept_description + "</h2>"
    
    html_text_2 = '''
    <div class="concept id="lesson-9-1"><h4><u>''' + concept_subtitle + "</h4></u>"
    
    html_text_3 = '''
    <p>''' + concept_body
    
    html_text_4 = '''
    </p>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3 + html_text_4
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    concept_subtitle = concept [2]
    concept_body = concept[3]
    return generate_concept_HTML(concept_title, concept_description, concept_subtitle, concept_body)

Brent_CONCEPTS = [ ['Lesson-9', 'Building HTML with Python', 'Art', 'Generating code to match my existing HTML file to add information using Python'],
                          ['Lesson-9', 'Adding Code with Python', 'Code', 'Setting up the parameters to add standard HTML code.  Need to know how to add to actual file'],
                          ['Lesson-9', 'Still Need a Loop', 'Defect', 'I can see a defect as I do not have view of how to build a look to increase 1 to 2...for the lessons but I like the idea to simplify and replicate HTML']]


def HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print HTML_for_many_concepts(Brent_CONCEPTS)
