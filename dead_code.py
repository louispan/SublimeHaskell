## Dead code: No references to these functions/classes in the source.

import SublimeHaskell.sublime_haskell_common as Common
import SublimeHaskell.parseoutput as ParseOutput

def run_build_commands_with(msg, cmds):
    """Run general build commands"""
    _, view, file_shown_in_view = Common.get_haskell_command_window_view_file_project()
    if not file_shown_in_view:
        return
    syntax_file_for_view = view.settings().get('syntax').lower()
    if 'haskell' not in syntax_file_for_view:
        return
    cabal_project_dir, cabal_project_name = Common.get_cabal_project_dir_and_name_of_view(view)
    if not cabal_project_dir:
        return

    ParseOutput.run_chain_build_thread(view, cabal_project_dir, msg(cabal_project_name), cmds, lambda x: x)


def run_build_command_with(msg, cmd):
    """Run one command"""
    run_build_commands_with(msg, [cmd])

## from parseoutput.py:


# def get_error_at(filename, line, column):
#     global ERRORS
#     for err in ERRORS:
#         if err.filename == filename and err.region.start.line == line and err.region.start.column:
#             return err
#     return None
