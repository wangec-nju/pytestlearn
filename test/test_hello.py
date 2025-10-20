import pytest
from package.hello import *
class HelloTest:

    @pytest.mark.parametrize("name",["NOVA","NJU","CAC"])
    def test_get_name(self,name):
        instance = Hello(name)
        assert instance.get_name() in ["NOVA","CAC"]
    
    @pytest.mark.parametrize("name",["NOVA","NJU","CAC"])
    def test_set_name(self,name):
        instance = Hello("NONONO")
        instance.set_name(name)
        assert (instance.get_name() == name and instance.get_name() != "NONONO")
    
    @pytest.mark.parametrize("name",["NOVA","NJU","CAC"])
    def test_say(self,name):
        instance = Hello(name)
        instance.say()