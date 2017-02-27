var portalLink = {
  name : "portalLink",
  data : function (){
        return {
            collapse : "collapse",
            sharp : "#"
        }
  },
  props : {
        parent : "",
        link : {}
    },

  template : "<div class='panel'>\
                <a class='panel-heading collapsed' href='panel-heading collapsed' role='tab' data-toggle='collapse'\
                :data-parent='sharp + parent' :href='sharp + collapse + parent + link.title'\
                aria-expanded='false'>\
                    <h4 class='panel-title'>{{ link.title }}</h4>\
                </a>\
                <div class='panel-collapse collapse' :id='collapse + parent + link.title'>{{ link.description }}</div>\
              </div>",
}

Vue.component("portalLink", portalLink);
