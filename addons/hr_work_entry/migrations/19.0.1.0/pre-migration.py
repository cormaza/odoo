# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

def migrate(cr, version):
    if not version:
        return
    # Rename XMLID from hr_payroll to hr_work_entry to prevent duplicate work entry type creation
    print("Pre-migration: Renaming hr_work_entry_type_out_of_contract XMLID module to hr_work_entry...")
    cr.execute("""
        UPDATE ir_model_data
        SET module = 'hr_work_entry'
        WHERE module = 'hr_payroll'
          AND name = 'hr_work_entry_type_out_of_contract'
          AND model = 'hr.work.entry.type';
    """)
    print("Pre-migration: hr_work_entry_type_out_of_contract XMLID module renamed successfully.")

    # Rename all XMLIDs from hr_work_entry_contract_enterprise to hr_work_entry_enterprise
    print("Pre-migration: Renaming all hr_work_entry_contract_enterprise XMLID modules to hr_work_entry_enterprise...")
    cr.execute("""
        UPDATE ir_model_data
        SET module = 'hr_work_entry_enterprise'
        WHERE module = 'hr_work_entry_contract_enterprise';
    """)
    print("Pre-migration: hr_work_entry_contract_enterprise XMLID modules renamed successfully.")

