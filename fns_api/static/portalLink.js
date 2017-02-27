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
                :data-parent='sharp + parent' :href='sharp + collapse + parent + link.lid'\
                aria-expanded='false'>\
                    <h4 class='panel-title'>{{ link.title }} <span class='label label-success pull-right'>Count : {{link.count}}</span></h4>\
                </a>\
                <div class='panel-collapse collapse' :id='collapse + parent + link.lid'>\
                   <div class='panel-body'>\
                        <img style='width : 100%' :src='link.image' alt=''>\
                        <a :href='link.url'><p> {{ link.description }} </p></a>\
                   </div>\
                </div>\
              </div>",
}

Vue.component("portalLink", portalLink);
