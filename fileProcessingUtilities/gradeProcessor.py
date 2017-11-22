"""This module processes grades copied from Genesis

"""

import re

loop_state_dict = dict(finished_class=False
                       , start_teacher_name=False
                       , append_last_name=False
                       , finished_teacher=False)
loop_value_dict = dict(temp_class_name=[]
                       , temp_teach_name=[]
                       , final_grade='')

with open('/Users/syeedode/junk/grades') as inputs:
    for line in inputs:
        ''' print(line) '''
        line = line.replace('\t',' ').replace('\n','')
        if re.search('^[A-Z]', line):
            temp_class_name = []
            finished_class = False
            temp_teach_name = []
            start_teacher_name = False
            append_last_name = False
            finished_teacher = False
            final_grade = ''
            for word in line.split(' '):
                word = word.strip()
                # print(word, end=' ')
                if word.__contains__("8-9"):
                    # print(word, end=' ')
                    temp_class_name.pop()
                    finished_class = True
                if not finished_class:
                    temp_class_name.append(word)
                    temp_class_name.append(' ')
                if finished_class:
                    if start_teacher_name or append_last_name:
                        temp_teach_name.append(word)
                        if append_last_name:
                            append_last_name = False
                            finished_teacher = True
                        if start_teacher_name:
                            temp_teach_name.append(' ')
                            start_teacher_name = False
                            append_last_name = True
                    if word == "40":
                        start_teacher_name = True
                if finished_teacher:
                    if word == "" or word == temp_teach_name[2]:
                        word = 'No grade found'
                    else:
                        final_grade = word
                        finished_teacher = False
            class_name = ''.join(temp_class_name).strip()
            length = temp_teach_name.__len__()
            teacher_name = ''.join(temp_teach_name[length::-1]).replace(',','').strip()
            if final_grade:
                print(class_name, teacher_name, final_grade, sep=', ')
