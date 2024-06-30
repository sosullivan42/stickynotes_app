from django.test import TestCase
from django.urls import reverse
from .models import StickyNote

# # Testing of the models.

class StickyNoteModelTest(TestCase): 
    def setUp(self): 
        StickyNote.objects.create(title='Test StickyNote', description = 'This is a test stickynote.', mark_as_complete = False, created_by='Test Creator')

    def test_stickynote_has_title(self): 
        stickynote = StickyNote.objects.get(id=1)
        self.assertEqual(stickynote.title, 'Test StickyNote')

    def test_stickynote_has_description(self): 
        stickynote = StickyNote.objects.get(id=1)
        self.assertEqual(stickynote.description, 'This is a test stickynote.')

    def test_stickynote_is_initally_marked_incomplete(self): 
        stickynote = StickyNote.objects.get(id=1)
        self.assertEqual(stickynote.mark_as_complete, False)

    def test_stickynote_has_creator(self): 
        stickynote = StickyNote.objects.get(id=1)
        self.assertEqual(stickynote.created_by, 'Test Creator')

# Testing of the application view.
class StickyNoteViewTest(TestCase): 
    @classmethod
    def setUpTestData(cls): 
        StickyNote.objects.create(
        title='Test StickyNote', description = 'This is a test stickynote.', mark_as_complete = False, created_by='Test Creator')

        StickyNote.objects.create(
        title='Test StickyNote', description = 'This is a test stickynote.', mark_as_complete = False, created_by='Test Creator')


    def test_stickynote_get_all_returns_all_stickynotes(self): 
        response = self.client.get(reverse('stickynotes'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'Test StickyNote')

    def test_stickynote_get_returns_stickynote(self): 
        stickynote = StickyNote.objects.get(id=1)
        response = self.client.get(reverse('stickynote', args=[stickynote.id]))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'Test StickyNote')

    def test_delete_should_remove_stickynote(self): 
        stickynotes = StickyNote.objects.all()
        initial_length = stickynotes.count()

        stickynote = StickyNote.objects.get(id=1)

        response = self.client.get(reverse('delete_stickynote', args=[stickynote.id]))

        final_length = StickyNote.objects.all().count()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(initial_length-1, final_length)