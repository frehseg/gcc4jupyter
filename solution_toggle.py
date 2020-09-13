from IPython.display import display, HTML
def load_ipython_extension(ipython):
  display(HTML('''<script>
  code_show=true;
  function solution_toggle() {
   if (code_show){
   $('.cm-comment:contains(@solution)').closest('div.input').hide();
   } else {
   $('.cm-comment:contains(@solution)').closest('div.input').show();
   }
   code_show = !code_show
  }
  $( document ).ready(solution_toggle);
  if($(IPython.toolbar.selector.concat(' > #toggle solution')).length == 0){
    IPython.toolbar.add_buttons_group([
          {
               'label'   : 'toggle solution',
               'icon'    : 'fa fa-angle-double-down',
               'callback': function(){
                   $( document ).ready(solution_toggle);
               }
          }
      ], 'toggle-solution');
  }
  </script>'''))

