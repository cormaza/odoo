from odoo import api, SUPERUSER_ID
from openupgradelib import openupgrade


_columns_copies = {
    "account_move": [("l10n_ec_sri_payment_id", None, None)],
}


def _remap_bank_data(env):
    _xmlids_renames = [
        (
            "l10n_ec_niif.central",
            "l10n_ec.bank_1",
        ),
        (
            "l10n_ec_niif.pichincha",
            "l10n_ec.bank_2",
        ),
        (
            "l10n_ec_niif.bguayaquil",
            "l10n_ec.bank_3",
        ),
        (
            "l10n_ec_niif.citibank",
            "l10n_ec.bank_4",
        ),
        (
            "l10n_ec_niif.loja",
            "l10n_ec.bank_5",
        ),
        (
            "l10n_ec_niif.machala",
            "l10n_ec.bank_6",
        ),
        (
            "l10n_ec_niif.pacifico",
            "l10n_ec.bank_7",
        ),
        (
            "l10n_ec_niif.internacional",
            "l10n_ec.bank_8",
        ),
        (
            "l10n_ec_niif.amazonas",
            "l10n_ec.bank_9",
        ),
        (
            "l10n_ec_niif.austro",
            "l10n_ec.bank_10",
        ),
        (
            "l10n_ec_niif.produbanco",
            "l10n_ec.bank_11",
        ),
        (
            "l10n_ec_niif.bolivariano",
            "l10n_ec.bank_12",
        ),
        (
            "l10n_ec_niif.manabi",
            "l10n_ec.bank_13",
        ),
        (
            "l10n_ec_niif.ruminahui",
            "l10n_ec.bank_14",
        ),
        (
            "l10n_ec_niif.litoral",
            "l10n_ec.bank_15",
        ),
        (
            "l10n_ec_niif.solidario",
            "l10n_ec.bank_16",
        ),
        (
            "l10n_ec_niif.procredit",
            "l10n_ec.bank_17",
        ),
        (
            "l10n_ec_niif.capital",
            "l10n_ec.bank_18",
        ),
        (
            "l10n_ec_niif.banecuador",
            "l10n_ec.bank_20",
        ),
        (
            "l10n_ec_niif.delbank",
            "l10n_ec.bank_25",
        ),
        (
            "l10n_ec_niif.bev",
            "l10n_ec.bank_26",
        ),
    ]
    openupgrade.rename_xmlids(env.cr, _xmlids_renames)


def _remap_tag_groups(env):
    _xmlids_renames = [
        (
            "l10n_ec_niif.tax_group_iva",
            "l10n_ec.tax_group_vat_12",
        ),
        (
            "l10n_ec_niif.tax_group_ice",
            "l10n_ec.tax_group_ice",
        ),
        (
            "l10n_ec_niif.tax_group_iva_0",
            "l10n_ec.tax_group_vat0",
        ),
        (
            "l10n_ec_niif.tax_group_iva_14",
            "l10n_ec.tax_group_vat14",
        ),
        (
            "l10n_ec_niif.tax_group_iva_15",
            "l10n_ec.tax_group_vat_15",
        ),
        (
            "l10n_ec_niif.tax_group_iva_13",
            "l10n_ec.tax_group_vat_13",
        ),
        (
            "l10n_ec_niif.tax_group_iva_5",
            "l10n_ec.tax_group_vat_05",
        ),
        (
            "l10n_ec_niif.tax_group_iva_exempt",
            "l10n_ec.tax_group_vat_exempt",
        ),
        (
            "l10n_ec_niif.tax_group_iva_no_apply",
            "l10n_ec.tax_group_vat_not_charged",
        ),
        (
            "l10n_ec_niif.tax_group_irbpnr",
            "l10n_ec.tax_group_irbpnr",
        ),
        (
            "l10n_ec_niif.tax_group_iva_withhold",
            "l10n_ec.tax_group_withhold_vat_sale",
        ),
        (
            "l10n_ec_niif.tax_group_renta_withhold",
            "l10n_ec.tax_group_withhold_income_sale",
        ),
        (
            "l10n_ec_niif.tax_group_isd",
            "l10n_ec.tax_group_outflows",
        ),
        (
            "l10n_ec_niif.tax_group_third_amounts",
            "l10n_ec.tax_group_others",
        ),
    ]
    openupgrade.rename_xmlids(env.cr, _xmlids_renames)


def _remap_partners(env):
    _xmlids_renames = [
        (
            "l10n_ec_niif.consumidor_final",
            "l10n_ec.ec_final_consumer",
        ),
        (
            "l10n_ec_niif.ec_social_security",
            "l10n_ec.ec_social_security",
        ),
        (
            "l10n_ec_niif.servicio_rentas_internas",
            "l10n_ec.ec_tax_authority",
        ),
    ]
    openupgrade.rename_xmlids(env.cr, _xmlids_renames)


def _remap_latam_document_type(env):
    _xmlids_renames = [
        (
            "l10n_ec_niif.ec_dt_01",
            "l10n_ec.ec_dt_01",
        ),
        (
            "l10n_ec_niif.ec_dt_02",
            "l10n_ec.ec_dt_02",
        ),
        (
            "l10n_ec_niif.ec_dt_03",
            "l10n_ec.ec_dt_03",
        ),
        (
            "l10n_ec_niif.ec_dt_04",
            "l10n_ec.ec_dt_04",
        ),
        (
            "l10n_ec_niif.ec_dt_05",
            "l10n_ec.ec_dt_05",
        ),
        (
            "l10n_ec_niif.ec_dt_08",
            "l10n_ec.ec_dt_08",
        ),
        (
            "l10n_ec_niif.ec_dt_09",
            "l10n_ec.ec_dt_09",
        ),
        (
            "l10n_ec_niif.ec_dt_11",
            "l10n_ec.ec_dt_11",
        ),
        (
            "l10n_ec_niif.ec_dt_12",
            "l10n_ec.ec_dt_12",
        ),
        (
            "l10n_ec_niif.ec_dt_15",
            "l10n_ec.ec_dt_15",
        ),
        (
            "l10n_ec_niif.ec_dt_16",
            "l10n_ec.ec_dt_16",
        ),
        (
            "l10n_ec_niif.ec_dt_18",
            "l10n_ec.ec_dt_18",
        ),
        (
            "l10n_ec_niif.ec_dt_19",
            "l10n_ec.ec_dt_19",
        ),
        (
            "l10n_ec_niif.ec_dt_20",
            "l10n_ec.ec_dt_20",
        ),
        (
            "l10n_ec_niif.ec_dt_21",
            "l10n_ec.ec_dt_21",
        ),
        (
            "l10n_ec_niif.ec_dt_22",
            "l10n_ec.ec_dt_22",
        ),
        (
            "l10n_ec_niif.ec_dt_23",
            "l10n_ec.ec_dt_23",
        ),
        (
            "l10n_ec_niif.ec_dt_24",
            "l10n_ec.ec_dt_24",
        ),
        (
            "l10n_ec_niif.ec_dt_41",
            "l10n_ec.ec_dt_41",
        ),
        (
            "l10n_ec_niif.ec_dt_42",
            "l10n_ec.ec_dt_42",
        ),
        (
            "l10n_ec_niif.ec_dt_43",
            "l10n_ec.ec_dt_43",
        ),
        (
            "l10n_ec_niif.ec_dt_44",
            "l10n_ec.ec_dt_44",
        ),
        (
            "l10n_ec_niif.ec_dt_45",
            "l10n_ec.ec_dt_45",
        ),
        (
            "l10n_ec_niif.ec_dt_47",
            "l10n_ec.ec_dt_47",
        ),
        (
            "l10n_ec_niif.ec_dt_48",
            "l10n_ec.ec_dt_48",
        ),
        (
            "l10n_ec_niif.ec_dt_49",
            "l10n_ec.ec_dt_49",
        ),
        (
            "l10n_ec_niif.ec_dt_50",
            "l10n_ec.ec_dt_50",
        ),
        (
            "l10n_ec_niif.ec_dt_51",
            "l10n_ec.ec_dt_51",
        ),
        (
            "l10n_ec_niif.ec_dt_52",
            "l10n_ec.ec_dt_52",
        ),
        (
            "l10n_ec_niif.ec_dt_294",
            "l10n_ec.ec_dt_294",
        ),
        (
            "l10n_ec_niif.ec_dt_344",
            "l10n_ec.ec_dt_344",
        ),
        (
            "l10n_ec_niif.ec_dt_364",
            "l10n_ec.ec_dt_364",
        ),
        (
            "l10n_ec_niif.ec_dt_370",
            "l10n_ec.ec_dt_370",
        ),
        (
            "l10n_ec_niif.ec_dt_371",
            "l10n_ec.ec_dt_371",
        ),
        (
            "l10n_ec_niif.ec_dt_372",
            "l10n_ec.ec_dt_372",
        ),
        (
            "l10n_ec_niif.ec_dt_373",
            "l10n_ec.ec_dt_373",
        ),
        (
            "l10n_ec_niif.ec_dt_03",
            "l10n_ec.ec_dt_03",
        ),
    ]
    openupgrade.rename_xmlids(env.cr, _xmlids_renames)


def _remap_identification_type(env):
    _xmlids_renames = [
        (
            "l10n_ec_niif.it_ruc",
            "l10n_ec.ec_ruc",
        ),
        (
            "l10n_ec_niif.it_cedula",
            "l10n_ec.ec_dni",
        ),
        (
            "l10n_ec_niif.it_pasaporte",
            "l10n_ec.ec_passport",
        ),
    ]
    openupgrade.rename_xmlids(env.cr, _xmlids_renames)


def _backup_fp_data_partners(env):
    # Add field to keep data of fiscal position, to remap in l10n_ec_edi
    env.cr.execute("""
    ALTER TABLE res_partner ADD COLUMN IF NOT EXISTS old_l10n_ec_niif_fp_id int4 REFERENCES account_fiscal_position(id)
    """)
    env.cr.execute("""
    update res_partner as rp set old_l10n_ec_niif_fp_id = q.property_account_position_id
    from (
        select rp.id, cast(replace(ip.value_reference, 'account.fiscal.position,', '') as integer) 
        as property_account_position_id
        from res_partner as rp
        LEFT OUTER JOIN ir_property ip ON 
            ip.res_id = CONCAT('res.partner,', rp.id) 
            AND ip.name = 'property_account_position_id'
        where ip.value_reference is not null                                                 
    ) as q
    where q.id = rp.id
    """)


def pre_init_hook(cr):
    env = api.Environment(cr, SUPERUSER_ID, {})
    openupgrade.copy_columns(env.cr, _columns_copies)
    openupgrade.logged_query(env.cr, """
    update account_move set l10n_ec_sri_payment_id = null where l10n_ec_sri_payment_id is not null;
    """)
    _remap_partners(env)
    _backup_fp_data_partners(env)
    _remap_latam_document_type(env)
    _remap_identification_type(env)
    _remap_tag_groups(env)
    _remap_bank_data(env)


def _remap_l10n_ec_niif_payment_types(env):
    codes_idx_map = [
        ("cp_01", "P1"),
        ("cp_15", "P15"),
        ("cp_16", "P16"),
        ("cp_17", "P17"),
        ("cp_18", "P18"),
        ("cp_19", "P19"),
        ("cp_20", "P20"),
    ]
    for old_code, new_code in codes_idx_map:
        old_code_id = env["ir.model.data"].search([
            ("module", "=", "l10n_ec_niff"),
            ("name", "=", old_code)
        ]).res_id
        new_code_id = env.ref(f"l10n_ec.{new_code}").id
        legacy_name = openupgrade.get_legacy_name("l10n_ec_sri_payment_id")
        if old_code_id and new_code_id:
            openupgrade.logged_query(
                env.cr,
                f"""
                UPDATE account_move set 
                l10n_ec_sri_payment_id = {new_code_id} 
                where {legacy_name} = {old_code_id}
                """,
            )


def _remap_fiscal_positions(env):

    def _get_xml_id(xml_id):
        module, name = xml_id.split(".")
        return env["ir.model.data"].search([
            ("module", "=", module),
            ("name", "=", name),
            ("model", "=", "account.fiscal.position"),
        ], limit=1).res_id

    def _update_properties(db_ids, new_id):
        for db_id in db_ids:
            env.cr.execute(f"""
            update ir_property set value_reference = 'account.fiscal.position,{new_id}'
            where value_reference = 'account.fiscal.position,{db_id}'
            """)

    national_fp_xml_ids = [
        "l10n_ec_niif_pyme.fp_persjur",
        "l10n_ec_niif_pyme.fp_contrespec",
        "l10n_ec_niif_pyme.fp_naturalesobl",
        "l10n_ec_niif_pyme.fp_estateles",
        "l10n_ec_niif_pyme.fp_naturalesnoobl",
    ]
    foreign_fp_xml_ids = [
        "l10n_ec_niif_pyme.fp_extranjero",
    ]
    for company in env["res.company"].search([]):
        national_fp_xml_ids += [
            f"l10n_ec_niif.{company.id}_fp_special_taxation_companies",
            f"l10n_ec_niif.{company.id}_fp_public_companies",
            f"l10n_ec_niif.{company.id}_fp_person_obligated_accounting",
            f"l10n_ec_niif.{company.id}_fp_person_leases",
            f"l10n_ec_niif.{company.id}_fp_person_professional",
            f"l10n_ec_niif.{company.id}_fp_person_rustic",
            f"l10n_ec_niif.{company.id}_fp_person_other",
            f"l10n_ec_niif.{company.id}_fp_others",
            f"l10n_ec_niif.{company.id}_fp_companies",
        ]
        foreign_fp_xml_ids += [
            f"l10n_ec_niif.{company.id}_fp_foreing_company_local",
            f"l10n_ec_niif.{company.id}_fp_foreing_person_local",
            f"l10n_ec_niif.{company.id}_fp_foreing_company_exports",
            f"l10n_ec_niif.{company.id}_fp_foreing_person_exports",
        ]
    national_fp = env.ref("l10n_ec.fp_local")
    foreign_fp = env.ref("l10n_ec.fp_foreign")
    national_db_ids = [_get_xml_id(xml_id) for xml_id in national_fp_xml_ids if _get_xml_id(xml_id)]
    foreign_db_ids = [_get_xml_id(xml_id) for xml_id in foreign_fp_xml_ids if _get_xml_id(xml_id)]

    _update_properties(national_db_ids, national_fp.id)
    _update_properties(foreign_db_ids, foreign_fp.id)


def _replace_taxes(env):
    tags_map = {
        "f104_411": "401",
        "f104_412": "402",
        "f104_413": "403",
        "f104_414": "404",
        "f104_415": "405",
        "f104_416": "406",
        "f104_417": "407",
        "f104_418": "408",
        "f104_435": "425",
        "f104_441": "431",
        "f104_444": "434",
        "f104_510": "500",
        "f104_512": "502",
        "f104_513": "503",
        "f104_514": "504",
        "f104_515": "505",
        "f104_516": "506",
        "f104_517": "507",
        "f104_518": "508",
        "f104_541": "531",
        "f104_542": "532",
        "f104_545": "535",
        "f104_550": "540",
    }
    account_tag_model = env["account.account.tag"]
    repartition_line_model = env["account.tax.repartition.line"]
    aml_model = env["account.move.line"]
    account_tag_datas = env["ir.model.data"].search([
        ("module", "=", "l10n_ec_niif"),
        ("model", "=", "account.account.tag")
    ])
    for account_tag_data in account_tag_datas:
        _, form_name, tag_code = account_tag_data.name.split("_")
        current_tax_map = tags_map.get(f"{form_name}_{tag_code}")
        new_tag_name = f"+{tag_code} (Reporte {form_name})"
        refund_tag_name = f"-{tag_code} (Reporte {form_name})"
        current_tag = account_tag_model.browse(account_tag_data.res_id)
        new_tag = account_tag_model.search([
            ("name", "=", new_tag_name),
            ("applicability", "=", "taxes"),
            ("id", "!=", account_tag_data.res_id)
        ])
        if new_tag:
            current_tag.name = new_tag_name
            new_tag.unlink()
        refund_tag = account_tag_model.search([
            ("name", "=", refund_tag_name)
        ])

        if current_tag:
            other_tag = False
            if current_tax_map:
                other_tag_name = f"+{tag_code} (Reporte {current_tax_map})"
                other_tag = account_tag_model.search([
                    ("name", "=", other_tag_name),
                ], limit=1)
                if other_tag:
                    aml_model.search([
                        ("tax_tag_ids", "=", current_tag.id),
                        ("move_id.move_type", "in", ["out_invoice", "in_invoice"])
                    ]).write({
                        "tag_ids": [(4, other_tag.id)]
                    })
            taxes_related = repartition_line_model.search([
                ("tag_ids", "in", current_tag.ids),
            ]).mapped("invoice_tax_id")
            for tax in taxes_related:
                base_invoice_repartition_line = tax.invoice_repartition_line_ids.filtered(
                    lambda x: x.repartition_type == "base"
                )
                if other_tag:
                    base_invoice_repartition_line.write({
                        "tag_ids": [(4, other_tag.id)]
                    })
                if refund_tag:
                    base_refund_repartition_line = tax.refund_repartition_line_ids.filtered(
                        lambda x: x.repartition_type == "base"
                    )
                    tags_to_replace = base_refund_repartition_line.tag_ids.filtered(
                        lambda x: x.id != refund_tag.id
                    )
                    base_refund_repartition_line.write({
                        "tag_ids": [(6, 0, refund_tag.ids)]
                    })
                    if tags_to_replace:
                        aml_model.search([
                            ("tax_tag_ids", "=", current_tag.id),
                            ("move_id.move_type", "in", ["out_refund", "in_refund"])
                        ]).write({
                            "tag_ids": [(4, other_tag.id)]
                        })


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    _remap_l10n_ec_niif_payment_types(env)
    _remap_fiscal_positions(env)
    _replace_taxes(env)
