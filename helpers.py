screen_helper = """
ScreenManager:
    TopScreen:
    LoginScreen:
    FirstScreen:
    FPCSScreen:
    RECScreen:
    OptionScreen:
    FullMenu1Screen:
    FullMenu2Screen:
    LastScreen:
<TopScreen>:
    name:'t_s'
    MDFloatLayout:
        MDLabel:
            text:"Welcome to KGB Food Ordering App"
            pos_hint:{"center_y": .65}
            font_style:"H4"
            halign:"center"
            theme_text_color:"Custom"
            text_color:1,0.6274509,0.0470588,1
        MDIconButton:
            icon:"arrow-right-bold-box"
            pos_hint: {"center_x": .5,"center_y": .35}
            size_hint_x: .5
            on_press: 
                root.manager.current = 'login_screen'
            theme_text_color: "Custom"
            text_color: 1,0.6274509,0.0470588,1           
<LoginScreen>:
    name:'login_screen'
    MDFloatLayout:
        MDLabel:
            text:"Sign Up"
            pos_hint:{"center_y": .75}
            front_style:"H5"
            halign:"center"
            theme_text_color:"Custom"
            text_color:1,0.6274509,0.0470588,1
        MDTextField:
            id:username
            hint_text: "Enter Username:"
            pos_hint: {"center_x": .5,"center_y": .65}
            current_hint_text_color:1,0.6274509,0.0470588,1
            size_hint_x: .7
        MDTextField:
            id:email
            hint_text: "Enter Email:"
            pos_hint: {"center_x": .5,"center_y": .5}
            current_hint_text_color:1,0.6274509,0.0470588,1
            size_hint_x: .7
        MDRaisedButton:
            text:"Log In"
            pos_hint: {"center_x": .75,"center_y": .35}
            size_hint_x: .25
            on_press: 
                root.save(username.text,email.text)
                root.manager.current = 'first'
            theme_text_color: "Custom"
            text_color: 0,0,0,1  
        MDIconButton:
            icon:"arrow-left-bold-box"
            pos_hint: {"center_x": .25,"center_y": .35}
            size_hint_x: .5
            on_press: 
                root.manager.current = 't_s'
            theme_text_color: "Custom"
            text_color: 1,0.6274509,0.0470588,1       
<FirstScreen>:
    name: 'first'
    MDFloatLayout:
        MDLabel:
            text : 'Do you want Recommender or Full Menu?'
            halign : 'center'
            pos_hint: {'center_y':0.7}
            text_color:1,0.6274509,0.0470588,1
        MDRectangleFlatButton:
            text: 'Recommender'
            pos_hint: {'center_x':0.5,'center_y':0.6}
            on_press: root.manager.current = 'fpcs'
        MDRectangleFlatButton:
            text: 'Full Menu'
            pos_hint: {'center_x':0.5,'center_y':0.4}
            on_press: root.manager.current = 'option_screen'
        MDIconButton:
            icon:"arrow-left-bold-box"
            pos_hint: {"center_x": .5,"center_y": .25}
            size_hint_x: .5
            on_press: 
                root.manager.current = 't_s'
            theme_text_color: "Custom"
            text_color: 1,0.6274509,0.0470588,1      
<FPCSScreen>:
    name: 'fpcs'
    course:course
    state:state
    MDFloatLayout:
        MDTextField:
            id: course
            hint_text: "Enter course"
            helper_text: "snack,main,dessert,starter"
            helper_text_mode: "on_focus"
            pos_hint:{'center_x': 0.5, 'center_y': 0.85}
            size_hint_x:None
            width:300
        MDTextField:
            id: state
            hint_text: "Enter state"
            helper_text: "enter as per the state's rto codes in small letters"
            helper_text_mode: "on_focus"
            pos_hint:{'center_x': 0.5, 'center_y': 0.7}
            size_hint_x:None
            width:300
        MDRectangleFlatButton:
            text: 'Submit'
            pos_hint: {'center_x':0.7,'center_y':0.4}
            on_press: 
                root.process()
                root.manager.current = 'rec_page'
        MDRectangleFlatButton:
            text: 'Back'
            pos_hint: {'center_x':0.3,'center_y':0.4}
            on_press: root.manager.current = 'first'
<OptionScreen>:
    name:'option_screen'
    MDFloatLayout:
        MDLabel:
            text : 'Do you want first part of the menu or the second part?'
            halign : 'center'
            pos_hint: {'center_y':0.7}
        MDRectangleFlatButton:
            text: 'First Part'
            pos_hint: {'center_x':0.5,'center_y':0.6}
            on_press: root.manager.current = 'f_p_m'
        MDRectangleFlatButton:
            text: 'Second Part'
            pos_hint: {'center_x':0.5,'center_y':0.5}
            on_press: root.manager.current = 's_p_m' 
        MDRectangleFlatButton:
            text: 'Back'
            pos_hint: {'center_x':0.5,'center_y':0.4}
            on_press: root.manager.current = 'first'           
<RECScreen>:
    name:'rec_page'
    order_list:order_list
    GridLayout:
        cols:1
        row_force_default:True
        row_default_height : 400
        ScrollView:
            MDList:
                id : container1
    MDTextField:
        id: order_list
        hint_text: "Enter your order here"
        helper_text: "enter every item with commas inbetween"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.25}
        size_hint_x:None
        width:300            
    MDRectangleFlatButton:
        text: 'place order'
        pos_hint: {'center_x':0.7,'center_y':0.1}
        on_press: 
            root.save_order()
            root.manager.current = 'last_screen'        
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.3,'center_y':0.1}
        on_press: root.manager.current = 'fpcs'   
<FullMenu1Screen>:
    name: 'f_p_m'
    order_list:order_list
    GridLayout:
        cols:1
        row_force_default:True
        row_default_height : 400
        ScrollView:
            MDList:
                id : container2
    MDTextField:
        id: order_list
        hint_text: "Enter your order here"
        helper_text: "enter every item with commas inbetween"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.25}
        size_hint_x:None
        width:300            
    MDRectangleFlatButton:
        text: 'place order'
        pos_hint: {'center_x':0.7,'center_y':0.1}
        on_press: 
            root.save_order()
            root.manager.current = 'last_screen'        
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.3,'center_y':0.1}
        on_press: root.manager.current = 'option_screen'
<FullMenu2Screen>:
    name: 's_p_m'
    order_list:order_list
    GridLayout:
        cols:1
        row_force_default:True
        row_default_height : 400
        ScrollView:
            MDList:
                id : container3
    MDTextField:
        id: order_list
        hint_text: "Enter your order here"
        helper_text: "enter every item with commas inbetween"
        helper_text_mode: "on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.25}
        size_hint_x:None
        width:300            
    MDRectangleFlatButton:
        text: 'place order'
        pos_hint: {'center_x':0.7,'center_y':0.1}
        on_press: 
            root.save_order()
            root.manager.current = 'last_screen'        
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.3,'center_y':0.1}
        on_press: root.manager.current = 'option_screen'  
          
        
<LastScreen>:
    name: 'last_screen'
    MDFloatLayout:
        MDLabel:
            text:'your order has been placed.'
            halign : 'center'
            pos_hint: {'center_y':0.7}
            font_style:'H4'       
    
        MDRectangleFlatButton:
            text: 'Back to login screen'
            pos_hint: {'center_x':0.3,'center_y':0.1}
            on_press: root.manager.current = 'login_screen' 
                   
"""
