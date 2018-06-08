from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from . import db_assistant

from .models import Project, Screen, Element, TestData, Action, Condition, Step, TestStep, Tag, TestCase, Cases, TestCycle



def create_new_tag(queryTag):
    tags_title_list = set()
    tags_list = Tag.objects.all()
    for t in tags_list:
        tags_title_list.add(t.title)

    if queryTag not in tags_title_list:
        newTag = Tag()
        newTag.title = queryTag
        newTag.save()


def create_new_screen(queryScreen):
    screen_title_list = set()
    screen_list = Screen.objects.all()
    for s in screen_list:
        screen_title_list.add(s.title)

    if queryScreen not in screen_title_list:
        newScreen = Screen()
        newScreen.title = queryScreen
        newScreen.save()

    return get_object_or_404(Screen, title=queryScreen)

def create_new_action(queryAction):
    action_title_list = set()
    action_list = Action.objects.all()
    for a in action_list:
        action_title_list.add(a.title)

    if queryAction not in action_title_list:
        newAction = Action()
        newAction.title = queryAction
        newAction.save()

    return get_object_or_404(Action, title=queryAction)


def create_new_element(queryElement):
    element_title_list = set()
    element_list = Element.objects.all()
    for e in element_list:
        element_title_list.add(e.title)

    if queryElement not in element_title_list:
        newElement = Element()
        newElement.title = queryElement
        newElement.save()

    return get_object_or_404(Element, title=queryElement)



def create_new_testdata(queryTestData):
    testdata_title_list = set()
    testdata_list = TestData.objects.all()
    for t in testdata_list:
        testdata_title_list.add(t.data)

    if queryTestData not in testdata_title_list:
        newTestData = TestData()
        newTestData.data = queryTestData
        newTestData.save()

    return get_object_or_404(TestData, data=queryTestData)



def create_new_condition(queryScreen, queryAction, queryElement, queryTestData):
    newCond = Condition()
    screen = create_new_screen(queryScreen)
    newCond.screen = screen
    action = create_new_action(queryAction)
    newCond.action = action


    if (queryElement):
        element = create_new_element(queryElement)
        newCond.element = element


    if (queryTestData):
        testdata = create_new_testdata(queryTestData)
        newCond.testdata = testdata

    newCond.save()


def create_new_step(queryScreen, queryAction, queryElement, queryTestData, queryExpResult):
    newStep = Step()
    condition = create_new_condition(queryScreen, queryAction, queryElement, queryTestData)
    newStep.condition = condition
    newStep.expresult = queryExpResult

    newStep.save()