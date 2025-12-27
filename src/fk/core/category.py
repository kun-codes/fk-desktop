#  Flowkeeper - Pomodoro timer for power users and teams
#  Copyright (c) 2023 Constantine Kulak
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
from __future__ import annotations

import datetime
import logging

from fk.core.abstract_data_container import AbstractDataContainer

logger = logging.getLogger(__name__)


def create_system_categories(root: Category, now: datetime.datetime) -> None:
    wg = root['#workitem_groups'] = Category('Workitem Groups', '#workitem_groups', True, "Info", root, now)

    gr = wg['#workitem_group_ABCDE'] = Category('ABCDE Method', '#workitem_group_ABCDE', True,
"""
The ABCDE method is a time management and prioritisation technique designed to help
individuals and teams organize tasks based on their importance and urgency. By
categorising tasks into five distinct groups, from most to least critical, this method
encourages a structured approach to tackling daily activities and projects.

- **A - Most important**: Tasks that are critical for your goals and have significant
consequences if not completed. These are your top priorities.
- **B - Important**: Tasks that are important but less critical than 'A' tasks. There are
moderate consequences if these are not completed.
- **C - Nice to do**: Activities that have no significant consequence whether done or not.
They are useful but not critical.
- **D - Delegate**: Tasks that can be assigned to someone else. They need to be done but not
necessarily by you.
- **E - Eliminate**: Tasks that offer no real value and can be removed from your list without
impacting your goals or productivity.

The key to making this ABCDE Method work is for you to now discipline yourself to start immediately on your "A-1" task. Stay at it until it is complete. Use your willpower to get going on this one job, the single most important task you could possibly be doing.

Eat the whole frog and don’t stop until it’s finished completely.

Details: [https://www.briantracy.com/blog/time-management/the-abcde-list-technique-for-setting-priorities/](https://www.briantracy.com/blog/time-management/the-abcde-list-technique-for-setting-priorities/)
""", wg, now)
    gr['#workitem_group_ABCDE_A'] = Category('A - Most important (significant consequences if not completed)', '#workitem_group_ABCDE_A', True,
"""
**"A" Items Are Most Important**

An A item is defined as something that is very important. This is something that you must do.

This is a task for which there can be serious consequences if you fail to do it. Consequences such as not visiting a key customer or not finishing a report for your boss that she needs for an upcoming board meeting.

These are the frogs of your life.

If you have more than one "A" task, you prioritize these tasks by writing A-1, A-2, A-3, and so on in front of each item. Your A-1 task is your biggest, ugliest frog of all.
""", gr, now)
    gr['#workitem_group_ABCDE_B'] = Category('B - Important (moderate consequences if not completed)', '#workitem_group_ABCDE_B', True,
"""
**"B" Items Only Have Minor Consequences**

A B item is defined as a task that you should do. But it only has mild consequences.

These are the tadpoles of your work life. This means that someone may be unhappy or inconvenienced if you don’t do it, but it is nowhere as important as an A task. Returning an unimportant telephone message or reviewing your email would be a B task.

The rule is that you should never do a B task when there is an A task left undone. You should never be distracted by a tadpole when there is a big frog sitting there waiting to be eaten.
""", gr, now)
    gr['#workitem_group_ABCDE_C'] = Category('C - Nice to do (no significant consequence whether done or not)', '#workitem_group_ABCDE_C', True,
"""
**"C" Tasks Have No Consequences**

A C task is something that would be nice to do, but for which there are no consequences at all, whether you do it or not.

C tasks include phoning a friend, having coffee or lunch with a coworker or completing some personal business during work hours. This sort of activity has no effect at all on your work life.

As a rule, you can never complete a C task when there are B or A tasks left undone.
""", gr, now)
    gr['#workitem_group_ABCDE_D'] = Category('D - Delegate (need to be done but not necessarily by you)', '#workitem_group_ABCDE_D', True,
"""
**"D" for Delegate**

A D activity is something that you can delegate to someone else.

The rule is that you should delegate everything that you possibly can to other people. This frees up more time for you to engage in your A activities. Your A tasks and their completion, largely determine the entire course of your career.
""", gr, now)
    gr['#workitem_group_ABCDE_E'] = Category('E - Eliminate (offer no real value and can be removed)', '#workitem_group_ABCDE_E', True,
"""
**"E" for Eliminate**

An E activity is something that you should eliminate altogether.

After all, you can only get your time under control if you stop doing things that are no longer necessary for you to do.
""", gr, now)

    gr = wg['#workitem_group_Eisenhower'] = Category('Eisenhower Matrix', '#workitem_group_Eisenhower', True,
"""
Details: [https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf](https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf)
""", wg, now)
    gr['#workitem_group_Eisenhower_U_I'] = Category('Urgent and Important (with deadlines or consequences)', '#workitem_group_Eisenhower_U_I', True,
"""
Details: [https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf](https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf)
""", gr, now)
    gr['#workitem_group_Eisenhower_U_NI'] = Category('Urgent and Not Important (require your attention, but do not have deadlines or consequences)', '#workitem_group_Eisenhower_U_NI', True,
"""
Details: [https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf](https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf)
""", gr, now)
    gr['#workitem_group_Eisenhower_NU_I'] = Category('Not Urgent and Important (with unclear deadlines that contribute to long-term success)', '#workitem_group_Eisenhower_NU_I', True,
"""
Details: [https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf](https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf)
""", gr, now)
    gr['#workitem_group_Eisenhower_NU_NI'] = Category('Not Urgent and Not Important (unnecessary, distractions, and time-wasters)', '#workitem_group_Eisenhower_NU_NI', True,
"""
Details: [https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf](https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf)
""", gr, now)

    gr = wg['#workitem_group_Pareto'] = Category('Pareto Principle', '#workitem_group_Pareto', True,
"""
Details: [https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf](https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf)
""", wg, now)
    gr['#workitem_group_Pareto_80'] = Category('80% Effort, 20% Outcomes', '#workitem_group_Pareto_80', True,
"""
Details: [https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf](https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf)
""", gr, now)
    gr['#workitem_group_Pareto_20'] = Category('20% Effort, 80% Outcomes', '#workitem_group_Pareto_20', True,
"""
Details: [https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf](https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf)
""", gr, now)

    gr = wg['#workitem_group_Buffet'] = Category("Warren Buffett's 5/25 Rule", '#workitem_group_Buffet', True,
"""
Details: [https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf](https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf)
""", wg, now)
    gr['#workitem_group_Buffet_5'] = Category('Top-5 Tasks (focus)', '#workitem_group_Buffet_5', True,
"""
Details: [https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf](https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf)
""", gr, now)
    gr['#workitem_group_Buffet_20'] = Category('Remaining 20 Tasks (eliminate)', '#workitem_group_Buffet_20', True,
"""
Details: [https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf](https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf)
""", gr, now)

    gr = wg['#workitem_group_333'] = Category("3-3-3 Method", '#workitem_group_333', True,
"""
Details: [https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf](https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf)
""", wg, now)
    gr['#workitem_group_333_1'] = Category('Most Important Thing (spend 3 hours on this)', '#workitem_group_333_1', True,
"""
Details: [https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf](https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf)
""", gr, now)
    gr['#workitem_group_333_2'] = Category('Short Tasks (maximum 3)', '#workitem_group_333_2', True,
"""
Details: [https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf](https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf)
""", gr, now)
    gr['#workitem_group_333_3'] = Category('Maintenance Activities (maximum 3)', '#workitem_group_333_3', True,
"""
Details: [https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf](https://sps.columbia.edu/sites/default/files/2023-08/Eisenhower%20Matrix.pdf)
""", gr, now)

    gr = wg['#workitem_group_MSCW'] = Category("MoSCoW Method", '#workitem_group_MSCW', True,
"""
Details: [https://en.wikipedia.org/wiki/MoSCoW_method](https://en.wikipedia.org/wiki/MoSCoW_method)
""", wg, now)
    gr['#workitem_group_MSCW_M'] = Category('M - Must have (failure if at least one is not done)', '#workitem_group_MSCW_M', True,
"""
Details: []()
""", gr, now)
    gr['#workitem_group_MSCW_S'] = Category('S - Should have (important but not necessary)', '#workitem_group_MSCW_S', True,
"""
Details: []()
""", gr, now)
    gr['#workitem_group_MSCW_C'] = Category('C - Could have (desirable but not necessary)', '#workitem_group_MSCW_C', True,
"""
Details: []()
""", gr, now)
    gr['#workitem_group_MSCW_W'] = Category("W - Won't have (least-critical or not appropriate)", '#workitem_group_MSCW_W', True,
"""
Details: []()
""", gr, now)

    gr = wg['#workitem_group_MSW'] = Category("Must, Should, Want", '#workitem_group_MSW', True,
"""
Details: [https://activecollab.com/blog/productivity/1-3-5-rule](https://activecollab.com/blog/productivity/1-3-5-rule)
""", wg, now)
    gr['#workitem_group_MSW_M'] = Category('I must...', '#workitem_group_MSW_M', True,
"""
Details: []()
""", gr, now)
    gr['#workitem_group_MSW_S'] = Category('I should...', '#workitem_group_MSW_S', True,
"""
Details: []()
""", gr, now)
    gr['#workitem_group_MSW_W'] = Category('I want to...', '#workitem_group_MSW_W', True,
"""
Details: []()
""", gr, now)

    gr = wg['#workitem_group_jar'] = Category("Pickle Jar Method", '#workitem_group_jar', True,
"""
Details: [https://en.wikipedia.org/wiki/MoSCoW_method](https://en.wikipedia.org/wiki/MoSCoW_method)
""", wg, now)
    gr['#workitem_group_jar_rocks'] = Category('Rocks (big, important goals or tasks)', '#workitem_group_jar_rocks', True,
"""
Details: []()
""", gr, now)
    gr['#workitem_group_jar_pebbles'] = Category('Pebbles (urgent but non-essential tasks)', '#workitem_group_jar_pebbles', True,
"""
Details: []()
""", gr, now)
    gr['#workitem_group_jar_sand'] = Category('Sand (small distractions and busywork)', '#workitem_group_jar_sand', True,
"""
Details: []()
""", gr, now)
    gr['#workitem_group_jar_water'] = Category("Water (private life, downtime, or hobbies)", '#workitem_group_jar_water', True,
"""
Details: []()
""", gr, now)

    root['#workitem_shares'] = Category('Workitem Shares', '#workitem_shares', True, "Info", root, now)
    root['#workitem_integrations'] = Category('Workitem Integrations', '#workitem_integrations', True, "Info", root, now)
    root['#workitem_tags'] = Category('Workitem Tags', '#workitem_tags', True, "Info", root, now)

    root['#backlog_groups'] = Category('Backlog Groups', '#backlog_groups', True, "Info", root, now)
    root['#backlog_shares'] = Category('Backlog Shares', '#backlog_shares', True, "Info", root, now)
    root['#backlog_integrations'] = Category('Backlog Integrations', '#backlog_integrations', True, "Info", root, now)
    root['#backlog_tags'] = Category('Backlog Tags', '#backlog_tags', True, "Info", root, now)


# TODO: Do not allow delimiters in category names
class Category(AbstractDataContainer['Category', 'Category|User']):
    _is_system: bool
    _info: str
    _uses: set['AbstractCategorizedDataContainer']

    def __init__(self,
                 name: str,
                 uid: str,
                 is_system: bool,
                 info: str,
                 parent: 'Category|User',
                 create_date: datetime.datetime):
        super().__init__(name=name,
                         uid=uid,
                         parent=parent,
                         create_date=create_date)
        self._is_system = is_system
        self._info = info
        self._uses = set()

    def __str__(self):
        return f'Category {self.get_uid()} - {self._name}{" (system)" if self._is_system else ""}, {len(self._uses)} uses'

    def is_root(self) -> bool:
        return self.get_uid() == '#root'

    def is_system(self) -> bool:
        return self._is_system

    def dump(self, indent: str = '', mask_uid: bool = False, mask_last_modified: bool = False) -> str:
        return f'{super().dump(indent, mask_uid, mask_last_modified)}\n' \
               f'{indent}  System: {self._is_system}' \
               f'{indent}  Info: {("<" + len(self._info) + "> characters") if self._info is not None else "None"}' \
               f'{indent}  Uses: <{len(self._uses)}>'

    def get_info(self):
        return self._info

    def to_dict(self) -> dict:
        d = super().to_dict()
        d['is_system'] = self._is_system
        return d

    def add_usage(self, usage: 'AbstractCategorizedDataContainer'):
        self._uses.add(usage)

    def remove_usage(self, usage: 'AbstractCategorizedDataContainer'):
        self._uses.delete(usage)

    def get_uses(self):
        return self._uses
