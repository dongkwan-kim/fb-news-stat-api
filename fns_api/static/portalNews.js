var portalNews = {
    props : {
        portals : {}
    },
    template : "<div >\
          <div class='row'>\
            <div class='col-md-12 col-sm-12 col-xs-12'>\
                <portal v-for='portal in portals' :portal='portal' :key='portal.id'></portal>\
                <div class='clearfix'></div>\
              </div>\
            </div>\
\
          <br />\
    </div>"
}

Vue.component('portalNews', portalNews);
