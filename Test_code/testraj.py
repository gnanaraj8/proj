from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import data
import time
import pytest

class Test_Raj:
    url="https://opensource-demo.orangehrmlive.com/"

    @pytest.fixture()
    def present_function(self):
        self.driver= webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(4)
        self.driver.close()

    def test_pim_01(self,present_function):
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.username_name).send_keys(data.Raj_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.password_name).send_keys(data.Raj_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Raj_Login_Data.login_button_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).click()
        time.sleep(3)
        search=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_a)
        print(search.is_displayed())
        time.sleep(4)    
        search_1=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_a_cap)
        print(search_1.is_displayed())
        time.sleep(3)
        search_2=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_b)
        print(search_2.is_displayed())
        time.sleep(3)
        search_3=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_b_cap)
        print(search_3.is_displayed())
        time.sleep(4)
        search_4=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_c)
        print(search_4.is_displayed())
        time.sleep(3)
        search_5=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_c_cap)
        print(search_5.is_displayed())
        time.sleep(3)
        search_6=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_d)
        print(search_6.is_displayed())
        time.sleep(4)
        search_7=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_d_cap)
        print(search_7.is_displayed())
        time.sleep(4)
        search_8=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_e)
        print(search_8.is_displayed())
        time.sleep(3)
        search_9=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_e_cap)
        print(search_9.is_displayed())
        time.sleep(4)
        search_10=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_f)
        print(search_10.is_displayed())
        time.sleep(4)
        search_11=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_f_cap)
        print(search_11.is_displayed())
        time.sleep(4)
        search_12=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_g)
        print(search_12.is_displayed())
        time.sleep(4)
        search_13=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_g_cap)
        print(search_13.is_displayed())
        time.sleep(4)
        search_14=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_h)
        print(search_14.is_displayed())
        time.sleep(4)
        search_15=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_h_cap)
        print(search_15.is_displayed())
        time.sleep(4)
        search_16=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_i)
        print(search_16.is_displayed())
        time.sleep(4)
        search_17=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_i_cap)
        print(search_17.is_displayed())
        time.sleep(4)
        search_18=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_j)
        print(search_18.is_displayed())
        time.sleep(4)
        search_19=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_j_cap)
        print(search_19.is_displayed())
        time.sleep(4)
        search_20=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_k)
        print(search_20.is_displayed())
        time.sleep(4)
        search_21=self.driver.find_element(by=By.XPATH, value=data.Pim_01_Search_Data.search_button_xpath).send_keys( data.Pim_01_Data.search_K_cap)
        print(search_21.is_displayed())
        assert self.driver.title=="OrangeHRM"
        print("passed")

    def test_pim_02(self, present_function):
        self.driver.get(self.url)
        time.sleep(4)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.username_name).send_keys(data.Raj_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.password_name).send_keys(data.Raj_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Raj_Login_Data.login_button_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_02.select_admin).click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_02.select_user_role).click()
        Element=self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_02.select_user_admin)
        for opt in Element:
            if opt.text == "Admin":
                opt.click()
                break
        time.sleep(4)        
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_02.select_status).click()
        Element_ele = self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_02.select_enabled)
        for obj in Element_ele:
            if obj.text == "Enabled":
                obj.click()
                break   
        time.sleep(4)      
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_02.select_uesr_role).click()
        Element_ess=self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_02.select_uesr_ess)
        for ops in Element_ess:
            if ops.text == "Ess":
                ops.click()
                break 
        time.sleep(4)       
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_02.select_statu).click()
        Element_dis = self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_02.select_disabled)
        for obt in Element_dis:
            if obt.text == "Disabled":
                obt.click()
        assert self.driver.title=="OrangeHRM"
        print("passed")    
    
    def test_pim_03(self,present_function):
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.username_name).send_keys(data.Raj_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.password_name).send_keys(data.Raj_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Raj_Login_Data.login_button_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.select_pim).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.select_add_button).click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.input_firstname).send_keys(data.Pim_03.firstname)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.input_lastname).send_keys(data.Pim_03.lastname)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.input_employeeid).clear()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.input_employeeid).send_keys(data.Pim_03.employeeid)
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.select_create_login).click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.input_username).send_keys(data.Pim_03.username)
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.password).send_keys(data.Pim_03.password)
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.confrim_pass).send_keys(data.Pim_03.confrimpass)
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.save_button).click()
        time.sleep(4)
        assert self.driver.title=="OrangeHRM"
        print("passed")

    def test_pim_04(self, present_function):
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.username_name).send_keys(data.Raj_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.password_name).send_keys(data.Raj_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Raj_Login_Data.login_button_xpath).click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.select_pim).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_04.select_employee).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_04.select_employee_contact).is_selected()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_04.select_employee_emergency).is_selected()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_04.select_employee_dependent).is_selected()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_04.select_employee_immigration).is_selected()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_04.select_employee_job).is_selected()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_04.select_employee_salary).is_selected()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_04.select_employee_tax).is_selected()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_04.select_employee_report).is_selected()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_04.select_employee_qualification).is_selected()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_04.select_employee_membership).is_selected()
        assert self.driver.title=="OrangeHRM"
        print("passed")

    def test_pim_05(self,present_function):
        self.driver.get(self.url)
        time.sleep(4)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.username_name).send_keys(data.Raj_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.password_name).send_keys(data.Raj_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Raj_Login_Data.login_button_xpath).click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.select_pim).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_05_Data.select_myprofile_xpath).click()
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.input_firstname).clear()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.input_firstname).send_keys(data.Pim_03.firstname)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.input_lastname).clear()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.input_lastname).send_keys(data.Pim_03.lastname)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.input_employeeid).clear()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.input_employeeid).send_keys(data.Pim_03.employeeid)
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_05_Data.input_nickname_xpath).send_keys(data.Tc_Pim_Data.nickname)
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_05_Data.input_license_xpath).send_keys(data.Tc_Pim_Data.license)
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_05_Data.input_license_date_xpath).send_keys(data.Tc_Pim_Data.license_date)
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_05_Data.input_ssn_number_xpath).send_keys(data.Tc_Pim_Data.ssn_numbr)
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_05_Data.input_sin_number_xpath).send_keys(data.Tc_Pim_Data.sin_number)
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_05_Data.select_nationality_xpath).click()
        Element_am = self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_05_Data.select_am_xpath)
        for cho in Element_am:
            if cho.text == "American":
                cho.click()
                break 
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_05_Data.select_marital_status_xpath).click()
        Status = self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_05_Data.select_married_status_xpath)
        for sel in Status:
            if sel.text == "Married":
                sel.click()
                break
        time.sleep(6)     
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_05_Data.select_date_of_birth_status_xpath).send_keys(data.Tc_Pim_Data.date_of_birth)
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_05_Data.select_gender_xpath).click()
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_05_Data.input_military_service_xpath).send_keys(data.Tc_Pim_Data.military_service)
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_05_Data.select_smoke_checkbox_xpath).click()
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_05_Data.select_save_xpath).click()
        assert self.driver.title=="OrangeHRM"
        print("passed")

    def test_pim_06(self,present_function):
        self.driver.get(self.url)
        time.sleep(4)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.username_name).send_keys(data.Raj_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.password_name).send_keys(data.Raj_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Raj_Login_Data.login_button_xpath).click()
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.select_pim).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_05_Data.select_myprofile_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_06_Data.select_contact_xpath).click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_06_Data.input_street_01_xpath).send_keys(data.Pim_06.street_01)
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_06_Data.input_street_02_xpath).send_keys(data.Pim_06.street_02)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_06_Data.input_city_xpath).send_keys(data.Pim_06.city)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_06_Data.input_state_xpath).send_keys(data.Pim_06.state)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_06_Data.input_zip_code_xpath).send_keys(data.Pim_06.zip_code)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_06_Data.select_country_xpath).click()
        Us = self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_06_Data.select_us_xpath)
        for sel in Us:
            if sel.text == "United States":
                sel.click()
                break
        time.sleep(4)    
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_06_Data.input_home_xpath).send_keys(data.Pim_06.home)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_06_Data.input_mobile_xpath).send_keys(data.Pim_06.mobile)
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_06_Data.input_work_xpath).send_keys(data.Pim_06.work)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_06_Data.input_work_email_xpath).send_keys(data.Pim_06.work_email)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_06_Data.input_other_email_xpath).send_keys(data.Pim_06.other_mail)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_06_Data.save_button_xpath).click()
        assert self.driver.title=="OrangeHRM"
        print("passed")

    def test_pim_07(self,present_function):
        self.driver.get(self.url)
        time.sleep(4)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.username_name).send_keys(data.Raj_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.password_name).send_keys(data.Raj_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Raj_Login_Data.login_button_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.select_pim).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_05_Data.select_myprofile_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_07_Data.select_emergency_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_07_Data.select_add_button_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_07_Data.input_name_xpath).send_keys(data.Pim_07.name)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_07_Data.input_relationship_xpath).send_keys(data.Pim_07.relationship)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_07_Data.input_home_tele_xpath).send_keys(data.Pim_07.home_tele)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_07_Data.input_mobile_xpath).send_keys(data.Pim_07.mobile)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_07_Data.input_work_tele_xpath).send_keys(data.Pim_07.work_tele)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_07_Data.save_button).click()
        assert self.driver.title=="OrangeHRM"
        print("passed")

    def test_pim_08(self, present_function):    
        self.driver.get(self.url)
        time.sleep(4)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.username_name).send_keys(data.Raj_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.password_name).send_keys(data.Raj_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Raj_Login_Data.login_button_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.select_pim).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_05_Data.select_myprofile_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_08_Data.select_dependents_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_08_Data.select_add_button_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_08_Data.input_name_xpath).send_keys(data.Pim_07.name)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_08_Data.select_relationship_xpath).click()
        Others = self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_08_Data.select_others_xpath)
        for sel in Others:
            if sel.text == "Other":
                sel.click()
                break
        time.sleep(3)    
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_08_Data.input_specify_xpath).send_keys(data.Pim_07.specify)
        time.sleep(3)    
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_08_Data.input_date_of_birth_xpath).send_keys(data.Pim_07.date_of_birth)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_08_Data.save_button).click()
        assert self.driver.title=="OrangeHRM"
        print("passed")

    def test_pim_09(self,present_function):    
        self.driver.get(self.url)
        time.sleep(4)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.username_name).send_keys(data.Raj_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.password_name).send_keys(data.Raj_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Raj_Login_Data.login_button_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.select_pim).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_05_Data.select_myprofile_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_09_Data.select_job_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_09_Data.input_joined_date_xpath).send_keys(data.Pim_09.join_date)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_09_Data.select_job_title_xpath).click()
        Finance = self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_09_Data.select_finance_manager_xpath)
        for sel in Finance:
            if sel.text == "Finance Manager":
                sel.click()
                break
        time.sleep(3)    
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_09_Data.input_job_specification_xpath).send_keys(data.Pim_09.job_specification)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_09_Data.select_job_category_xpath).click()
        Pro = self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_09_Data.select_professionals_xpath)
        for sel in Pro:
            if sel.text == "Professionals":
                sel.click()
                break
        time.sleep(3)    
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_09_Data.select_sub_unit_xpath).click()
        Fin = self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_09_Data.select_finance_xpath)
        for sel in Fin:
            if sel.text == "Finance":
                sel.click()
                break
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_09_Data.select_location_xpath).click()
        Ca = self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_09_Data.select_ca_us_xpath)
        for sel in Ca:
            if sel.text == "HQ - CA, USA":
                sel.click()
                break
        time.sleep(3)    
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_09_Data.select_employ_status_xpath).click()
        Full = self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_09_Data.select_full_time_xpath)
        for sel in Full:
            if sel.text == "Full-Time Permanent":
                sel.click()
                break
        time.sleep(3)    
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_09_Data.select_button_contract_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_09_Data.input_contract_start_xpath).send_keys(data.Pim_09.contract_start)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_09_Data.input_contract_end_xapath).send_keys(data.Pim_09.contract_end)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_09_Data.save_button).click()
        assert self.driver.title=="OrangeHRM"
        print("passed")

    def test_pim_10(self,present_function):    
        self.driver.get(self.url)
        time.sleep(4)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.username_name).send_keys(data.Raj_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.password_name).send_keys(data.Raj_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Raj_Login_Data.login_button_xpath).click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.select_pim).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_05_Data.select_myprofile_xpath).click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_10_Data.select_terminated_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_10_Data.select_terminate_date).send_keys(data.Pim_09.ter_date)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_10_Data.select_reason).click()
        Res = self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_10_Data.select_resigned)
        for sel in Res:
            if sel.text == "Resigned":
                sel.click()
                break
        time.sleep(3)    
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_10_Data.input_note).send_keys(data.Pim_09.note)
        time.sleep(3)     
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_10_Data.save_button).click()
        assert self.driver.title=="OrangeHRM"
        print("passed")

    def test_pim_12(self,present_function):
        self.driver.get(self.url)
        time.sleep(4)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.username_name).send_keys(data.Raj_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.password_name).send_keys(data.Raj_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Raj_Login_Data.login_button_xpath).click()
        time.sleep(3) 
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.select_pim).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_05_Data.select_myprofile_xpath).click()
        time.sleep(3) 
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_12_Data.select_salary).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_12_Data.select_add_button).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_12_Data.input_salary_component).send_keys(data.Pim_12.component)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_12_Data.select_pay_grade).click()
        Gra = self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_12_Data.select_grade3)
        for sel in Gra:
            if sel.text == "Grade 3":
                sel.click()
                break
        time.sleep(4)    
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_12_Data.select_pay_frequency).click()
        Month = self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_12_Data.select_monthly)
        for sel in Month:
            if sel.text == "Monthly":
                sel.click()
                break
        time.sleep(4)    
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_12_Data.select_currency).click()
        Us_Dr = self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_12_Data.select_monthly)
        for sel in Us_Dr:
            if sel.text == "United States Dollar":
                sel.click()
                break
        time.sleep(4)    
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_12_Data.input_amound).send_keys(data.Pim_12.amount)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_12_Data.select_direct_button).click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_12_Data.input_acc_no).send_keys(data.Pim_12.acc_no)
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_12_Data.select_acc_type).click()
        Save = self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_12_Data.select_savings)
        for sel in Save:
            if sel.text == "Savings":
                sel.click()
                break
        time.sleep(4)    
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_12_Data.input_routing_no).send_keys(data.Pim_12.routing_no)
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_12_Data.input_amound).send_keys(data.Pim_12.in_amount)
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_12_Data.save_button).click()

    def test_pim_13(self,present_function):
        self.driver.get(self.url)
        time.sleep(4)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.username_name).send_keys(data.Raj_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Raj_Login_Data.password_name).send_keys(data.Raj_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Raj_Login_Data.login_button_xpath).click()
        time.sleep(4) 
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_03.select_pim).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_05_Data.select_myprofile_xpath).click()
        time.sleep(4)   
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_13_Data.select_tax).click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_13_Data.select_status).click()
        Marry = self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_13_Data.select_married)
        for sel in Marry:
            if sel.text == "Married":
                sel.click()
                break
        time.sleep(4)    
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_13_Data.input_exemption).send_keys(data.Pim_13.exemption)
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=data.Tc_Pim_13_Data.select_state_income_tax).click()
        Alas = self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_13_Data.select_alaska)
        for sel in Alas:
            if sel.text == "Alaska":
                sel.click()
                break
        time.sleep(4)    
        self.driver.find_element(by=By.XPATH, Value=data.Tc_Pim_13_Data.select_statu).click()
        Marrie = self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_13_Data.select_marrie)
        for sel in Marrie:
            if sel.text == "Married":
                sel.click()
                break
        time.sleep(4)    
        self.driver.find_element(by=By.XPATH, Value=data.Tc_Pim_13_Data.input_state_exemption).send_keys(data.Pim_13.state_exemption)
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, Value=data.Tc_Pim_13_Data.select_unemp_state).click()
        Marry = self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_13_Data.select_marry)
        for sel in Marry:
            if sel.text == "Married":
                sel.click()
                break
        time.sleep(4)    
        self.driver.find_element(by=By.XPATH, Value=data.Tc_Pim_13_Data.select_work).click()
        Alask = self.driver.find_elements(by=By.XPATH, value=data.Tc_Pim_13_Data.select_wrk_ala)
        for sel in Alask:
            if sel.text == "Alaska":
                sel.click()
                break
        time.sleep(4)    
        self.driver.find_element(by=By.XPATH, Value=data.Tc_Pim_13_Data.save_button).click()
        assert self.driver.title=="OrangeHRM"
        print("passed")