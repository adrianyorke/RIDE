#  Copyright 2008 Nokia Siemens Networks Oyj
#  
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  
#      http://www.apache.org/licenses/LICENSE-2.0
#  
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


from robotide.model.files import TestCaseFile, ResourceFile, InitFile,\
    _EmptyResourceFile, _EmptyTestSuite
from robotide.model.tcuk import UserKeyword, TestCase


class MockSerializer(object):
    
    def __init__(self):
        self.record = []

    def close(self):
        self.record = []
        
    def start_settings(self):
        self.record.append('Start Settings')
        
    def setting(self, name, value):
        self.record.append('Setting: %s | %s' % (name, value))

    def documentation(self, doc):
        self.record.append('Documentation: %s' % doc)

    def end_settings(self):
        self.record.append('End Settings')
    
    def start_variables(self):
        self.record.append('Start Variables')
        
    def variable(self, name, value):
        self.record.append('Variable: %s | %s' % (name, value))    
    
    def end_variables(self):
        self.record.append('End Variables')
        
    def start_testcases(self):
        self.record.append('Start Test Cases')
        
    def end_testcases(self):
        self.record.append('End Test Cases')
        
    def start_keywords(self):
        self.record.append('Start User Keywords')

    def end_keywords(self):
        self.record.append('End User Keywords')
        
    def start_testcase(self, test):
        self.record.append('Start Test: %s' % test.name)
    
    def end_testcase(self):
        self.record.append('End Test')
    
    def start_keyword(self, uk):
        self.record.append('Start UK: %s' % uk.name)
        
    def end_keyword(self):
        self.record.append('End UK')
        
    def keyword(self, kw):
        self.record.append('KW: %s' % kw.name)
        

class FakeResource(ResourceFile):

    def __init__(self, name='Fake Resource', doc='', path='fake/resource.html'):
        data = _EmptyResourceFile(path)
        ResourceFile.__init__(self, data)
        self.name = name
        self.doc = doc
        self.source = path

    def add_uk(self, name, doc=''):
        self.keywords.append(FakeUserKeyword(name, doc))

    def _get_mtime(self, path):
        return 0


class FakeDirectorySuite(InitFile):

    def __init__(self, name='Fake Dir Suite', doc='', path='fake/__init__.html'):
        data = _EmptyTestSuite(path)
        data.doc = doc
        data.initfile = path
        InitFile.__init__(self, data)
        self.name = name


class FakeSuite(TestCaseFile):

    def __init__(self, name='Fake Suite', doc='', path='fake/suite.html'):
        data = _EmptyTestSuite(path)
        data.doc = doc
        TestCaseFile.__init__(self, data)
        self.name = name


class FakeUserKeyword(UserKeyword):

    def __init__(self, datafile, name='Fake UK', doc='Some doc'):
        UserKeyword.__init__(self, datafile, name=name)
        self.settings.doc.set_str_value(doc)
        self.settings.args.set_str_value('${scalar}')
        self.settings.return_value.set_str_value('Message')
        self.keywords = [_FakeKeyword()]


class FakeTestCase(TestCase):
    
    def __init__(self, datafile, name='Fake Test', doc='Fake doc'):
        TestCase.__init__(self, datafile, name=name)
        self.settings.doc.set_str_value(doc)
        self.keywords = [_FakeKeyword()]
        
        
class _FakeKeyword(object):

    def __init__(self):
        self.name = 'Fake'
        self.doc = ''
        self.args = []
        self.type = ''


class _FakeModel(object):
    suite = None

class _FakeUIObject(object):
    Enable = InsertSeparator = Append = Connect = lambda *args: None
    Insert = FindMenu = GetMenuBar = GetMenu = lambda *args: _FakeUIObject()
    GetMenuItemCount = lambda s: 1
    notebook = property(lambda *args: _FakeUIObject())

class FakeApplication(object):
    frame = _FakeUIObject()
    model = _FakeModel()
    get_model = lambda s: _FakeModel()
    subscribe = lambda s, x, y: None
    get_menu_bar = lambda s: _FakeUIObject()
    get_notebook = lambda s: _FakeUIObject()
    get_frame = lambda s: _FakeUIObject()
    create_menu_item = lambda *args: None
