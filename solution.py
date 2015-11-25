#!/usr/bin/env python


#DEBUG 
DEBUG = 0 


###############################################################################################
#FUNCTION: parse_sentence
#INPUT: 
#       original_sentence is the input sentence
#       objects is the dictionary of sets of objects
#OUTPUT:
#       original_sentence is the same as the input original sentence
#       tagged_list is the list of words in the sentence that were tagged from the objects
#       untagged_list is the list of words in the sentence that were not tagged from the objects
#       class_tagged_sentence is the sentence with the tagged words replaced by object types
################################################################################################


def parse_sentence(original_sentence, objects):

    #STEP1 define vars
    tagged_list = []
    untagged_list = []
    lower_case_original_sentence = "" 
    class_tagged_sentence = "" 
    found_flag = 0
    
    
    #STEP2 sanity check and parse original_sentence
    if DEBUG:
        print original_sentence
    
    lower_case_original_sentence = original_sentence.lower()
    
    list_of_words = lower_case_original_sentence.split()
    
    if DEBUG:
        print list_of_words
    
        for word in list_of_words:
            print word
    
    
    #STEP2 sanity check and examine objects
    if DEBUG:
        print objects
    
        for element in objects:
            print element
            print objects[element]
    
    #replace elements in set with lowercase value
    for element in objects:
    
       temp_set = set() 
    
       while objects[element]:
           temp = objects[element].pop()
           #print "this is temp %s" % (temp)
           temp_lower = temp.lower()
           #print "this is temp_lower %s" % (temp_lower)
           temp_set.add(temp_lower)
    
       objects[element] = temp_set
    
    
    if DEBUG:
        for element in objects:
            print element
            print objects[element]
    
    
    #STEP3 search for each word in original_sentence in the hash value set
    for word in list_of_words:
        found_flag = 0
    
        for element in objects:
            if word in objects[element]:
                #print "FOUND word %s in object %s" % (word, element)
                tagged_list.append(word) 
                found_flag = 1
                break
            else:
                #print "NOT found word %s" % (word)
                found_flag = 0 
    
        #append to untagged_list
        if found_flag == 0:
            untagged_list.append(word)
    
        #create class tagged sentence 
        if found_flag == 1:
            class_tagged_sentence = class_tagged_sentence + " " + element
        else:
            class_tagged_sentence = class_tagged_sentence + " " + word 
    
    
    if DEBUG == 1:
        print original_sentence
        print tagged_list
        print untagged_list
        print class_tagged_sentence

    return(original_sentence, tagged_list, untagged_list, class_tagged_sentence)


################### TEST CASES #####################

#TEST1 basic test

test1_sentence = "Jack and Jill went up one hill to get two pails of water while I'm watching from the farm"

test1_objects = {'NAME': set(['Jack', 'Jill']),
         'NUM': set(['one', 'two', 'three', 'four', 'five']),
         'PLACE': set(['hill', 'farm'])}


test1_original_sentence, test1_tagged_list, test1_untagged_list, test1_class_tagged_sentence = parse_sentence(test1_sentence, test1_objects)

print "TEST1 results"
print "original_sentence = %s " % (test1_original_sentence)
print "tagged_list = %s " % (test1_tagged_list)
print "untagged_list = %s " % (test1_untagged_list)
print "class_tagged_sentence = %s " % (test1_class_tagged_sentence)


#TEST2 check plurals are not replaced

test2_sentence = "There are multiple Jacks and Jills that went to two farms to get four pails of water while I'm watching from the farm"

test2_objects = {'NAME': set(['Jack', 'Jill']),
         'NUM': set(['one', 'two', 'three', 'four', 'five']),
         'PLACE': set(['hill', 'farm'])}


test2_original_sentence, test2_tagged_list, test2_untagged_list, test2_class_tagged_sentence = parse_sentence(test2_sentence, test2_objects)

print "\n\nTEST2 results"
print "original_sentence = %s " % (test2_original_sentence)
print "tagged_list = %s " % (test2_tagged_list)
print "untagged_list = %s " % (test2_untagged_list)
print "class_tagged_sentence = %s " % (test2_class_tagged_sentence)


#TEST3 check for multiple occurences of objects

test3_sentence = "I saw Jack and Jill going to the farm with two empty buckets, but then Jack and Jill returned from the farm with two buckets full of water"

test3_objects = {'NAME': set(['Jack', 'Jill']),
         'NUM': set(['one', 'two', 'three', 'four', 'five']),
         'PLACE': set(['hill', 'farm'])}


test3_original_sentence, test3_tagged_list, test3_untagged_list, test3_class_tagged_sentence = parse_sentence(test3_sentence, test3_objects)

print "\n\nTEST3 results"
print "original_sentence = %s " % (test3_original_sentence)
print "tagged_list = %s " % (test3_tagged_list)
print "untagged_list = %s " % (test3_untagged_list)
print "class_tagged_sentence = %s " % (test3_class_tagged_sentence)


























