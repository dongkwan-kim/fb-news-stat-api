var portal = {
  name : "portal",
  props : {
        portal : {} 
    },

  template : "<div class='col-md-4 col-sm-4 col-xs-12'> \
                    <div class='x_panel tile'>\
                      <div class='x_title'>\
                        <h2>{{ portal.name }}</h2>\
                        <h4 style='float : right;'>Count : {{ portal.count }}</h4>\
                        <div class='clearfix'></div>\
                        </div>\
                        <div class='x_content'>\
                            <div class='accordion' :id='portal.name' role='tablist' aria-multiselectable='true'>\
                                <portal-link v-for='link in portal.link' :parent='portal.name' :link='link'></portal-link>\
                            </div>\
                        </div>\
                    </div>\
              </div>",
}

Vue.component("portal", portal);
