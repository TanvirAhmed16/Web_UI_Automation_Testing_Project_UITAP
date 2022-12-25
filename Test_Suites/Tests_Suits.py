import unittest
import HtmlTestRunner

from Test_Cases.DynamicID import DynamicIDTest
from Test_Cases.ClassAttribute import ClassAttributeTest
from Test_Cases.LoadDelays import LoadDelaysTest
from Test_Cases.AJAXData import AJAXDataTest
from Test_Cases.ClientSideDelay import ClientSideDelayTest
from Test_Cases.TextInput import TextInputTest
from Test_Cases.Scrollbers import ScrollbarsTest
from Test_Cases.DynamicTable import DynamicTableTest
from Test_Cases.VerifyText import VerifyTextTest
from Test_Cases.ProgressBar import ProgressBarTest
from Test_Cases.Visibility import VisibilityTest
from Test_Cases.SampleApp import SampleAppTest
from Test_Cases.MouseOver import MouseOverTest
from Test_Cases.NonBreakingSpace import NonBreakingSpaceTest
from Test_Cases.OverlappedElement import OverlappedElementTest
from Test_Cases.ShadowDOM import ShadowDOMTest
from Test_Cases.RandomTests import RandomTests

tc_dynamic_id = unittest.TestLoader().loadTestsFromTestCase(DynamicIDTest)
tc_class_attribute = unittest.TestLoader().loadTestsFromTestCase(ClassAttributeTest)
tc_load_delays = unittest.TestLoader().loadTestsFromTestCase(LoadDelaysTest)
tc_ajax_data = unittest.TestLoader().loadTestsFromTestCase(AJAXDataTest)
tc_client_side_delay = unittest.TestLoader().loadTestsFromTestCase(ClientSideDelayTest)
tc_text_input = unittest.TestLoader().loadTestsFromTestCase(TextInputTest)
tc_scrollbars = unittest.TestLoader().loadTestsFromTestCase(ScrollbarsTest)
tc_dynamic_table = unittest.TestLoader().loadTestsFromTestCase(DynamicTableTest)
tc_verify_text = unittest.TestLoader().loadTestsFromTestCase(VerifyTextTest)
tc_progress_bar = unittest.TestLoader().loadTestsFromTestCase(ProgressBarTest)
tc_visibility = unittest.TestLoader().loadTestsFromTestCase(VisibilityTest)
tc_sample_app = unittest.TestLoader().loadTestsFromTestCase(SampleAppTest)
tc_mouse_over = unittest.TestLoader().loadTestsFromTestCase(MouseOverTest)
tc_non_breaking_space = unittest.TestLoader().loadTestsFromTestCase(NonBreakingSpaceTest)
tc_overlapped_ele = unittest.TestLoader().loadTestsFromTestCase(OverlappedElementTest)
tc_shadow_dom = unittest.TestLoader().loadTestsFromTestCase(ShadowDOMTest)
tc_random_tests = unittest.TestLoader().loadTestsFromTestCase(RandomTests)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(verbosity=2, report_title="UITAP Test Reports",
                                                           report_name="UITAP Test Result",
                                                           descriptions="Acceptance Test",
                                                           output="..\\Reports", combine_reports=True))
