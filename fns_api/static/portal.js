var portal = {
  props : ["news"],
  template : "<div class='col-md-4 col-sm-4 col-xs-12>\
                <div class='x_panel tile fixed_height_320'>\
                  <div class='x_title'>{{ news }}</div>\
                </div>\
              </div>",
}

Vue.component("portal", portal);
