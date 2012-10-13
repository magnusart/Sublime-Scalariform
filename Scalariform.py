import sublime, sublime_plugin

class ScalariformCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    import os
    os.system("java -jar scalariform.jar " + self.view.file_name())
    (self_group, self_view_idx) = sublime.active_window().get_view_index(self.view)
 
    self_g_views = sublime.active_window().views_in_group(self_group)

    if(len(self_g_views)<=1):
      view_idx = 0
      i=0
      for v in sublime.active_window().views():
        if(v.id()==self.view.id()):
          view_idx = i
          break          
        i=i+1

      (other_group, other_view_idx) = sublime.active_window().get_view_index(sublime.active_window().views()[view_idx-1])
      active_view_other_group = sublime.active_window().active_view_in_group(other_group)
      sublime.active_window().focus_view(active_view_other_group)
    else:
      sublime.active_window().focus_view(sublime.active_window().views()[self_view_idx-1])
    
    sublime.active_window().focus_view(self.view)
