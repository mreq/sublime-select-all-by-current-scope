import sublime
import sublime_plugin
import re

class SelectAllByCurrentScope(sublime_plugin.TextCommand):
	def run(self, edit, scope_must_match = False):
		view = self.view
		sel = view.sel()
		scope_name = None

		(row, col) = view.rowcol(sel[0].begin())
		point = view.text_point(row, col)
		point_scope = view.scope_name(point)

		if scope_must_match:
			regex = re.compile(scope_must_match)
			scope_names = [ x for x in point_scope.split(' ') if regex.search(x) ]
			if len(scope_names) > 0:
				scope_name = scope_names[0]
			else:
				sublime.status_message('Current scope doesn\'t match "' + scope_must_match + '", sorry :(')
		else:
			scope_name = point_scope

		if scope_name:
			sublime.status_message('Selected everything with the "' + scope_name.strip() + '" scope.')

			for region in view.find_by_selector(scope_name):
				sel.add(region)
