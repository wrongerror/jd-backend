flag_base = {
    'scoreconsoffv2':   '',
    'scorebank':        '',
    'scoreconsoff':     '',
    'scorepettycashv1': '',
    'scorecust':        ''
}  # 申请记录
flag_apply = {
    # 多次申请
    'al_m3_gid_bank_selfnum':         '',
    'al_m3_gid_bank_allnum':          '',
    'al_m3_gid_bank_orgnum':          '',
    'al_m3_gid_notbank_selfnum':      '',
    'al_m3_gid_notbank_allnum':       '',
    'al_m3_gid_notbank_orgnum':       '',
    'al_m3_id_bank_selfnum':          '',
    'al_m3_id_bank_allnum':           '',
    'al_m3_id_bank_orgnum':           '',
    'al_m3_id_notbank_selfnum':       '',
    'al_m3_id_notbank_allnum':        '',
    'al_m3_id_notbank_orgnum':        '',
    'al_m3_cell_bank_selfnum':        '',
    'al_m3_cell_bank_allnum':         '',
    'al_m3_cell_bank_orgnum':         '',
    'al_m3_cell_notbank_selfnum':     '',
    'al_m3_cell_notbank_allnum':      '',
    'al_m3_cell_notbank_orgnum':      '',
    'al_m6_gid_bank_selfnum':         '',
    'al_m6_gid_bank_allnum':          '',
    'al_m6_gid_bank_orgnum':          '',
    'al_m6_gid_notbank_selfnum':      '',
    'al_m6_gid_notbank_allnum':       '',
    'al_m6_gid_notbank_orgnum':       '',
    'al_m6_id_bank_selfnum':          '',
    'al_m6_id_bank_allnum':           '',
    'al_m6_id_bank_orgnum':           '',
    'al_m6_id_notbank_selfnum':       '',
    'al_m6_id_notbank_allnum':        '',
    'al_m6_id_notbank_orgnum':        '',
    'al_m6_cell_bank_selfnum':        '',
    'al_m6_cell_bank_allnum':         '',
    'al_m6_cell_bank_orgnum':         '',
    'al_m6_cell_notbank_selfnum':     '',
    'al_m6_cell_notbank_allnum':      '',
    'al_m6_cell_notbank_orgnum':      '',
    'al_m12_gid_bank_selfnum':        '',
    'al_m12_gid_bank_allnum':         '',
    'al_m12_gid_bank_orgnum':         '',
    'al_m12_gid_notbank_selfnum':     '',
    'al_m12_gid_notbank_allnum':      '',
    'al_m12_gid_notbank_orgnum':      '',
    'al_m12_id_bank_selfnum':         '',
    'al_m12_id_bank_allnum':          '',
    'al_m12_id_bank_orgnum':          '',
    'al_m12_id_notbank_selfnum':      '',
    'al_m12_id_notbank_allnum':       '',
    'al_m12_id_notbank_orgnum':       '',
    'al_m12_cell_bank_selfnum':       '',
    'al_m12_cell_bank_allnum':        '',
    'al_m12_cell_bank_orgnum':        '',
    'al_m12_cell_notbank_selfnum':    '',
    'al_m12_cell_notbank_allnum':     '',
    'al_m12_cell_notbank_orgnum':     '',
    # 特殊名单
    'sl_id_abnormal':                 '',
    'sl_id_bank_bad':                 '',
    'sl_id_bank_overdue':             '',
    'sl_id_bank_fraud':               '',
    'sl_id_bank_lost':                '',
    'sl_id_bank_refuse':              '',
    'sl_id_p2p_bad':                  '',
    'sl_id_p2p_overdue':              '',
    'sl_id_p2p_fraud':                '',
    'sl_id_p2p_lost':                 '',
    'sl_id_p2p_refuse':               '',
    'sl_id_phone_overdue':            '',
    'sl_id_court_bad':                '',
    'sl_id_court_executed':           '',
    'sl_id_nbank_p2p_bad':            '',
    'sl_id_nbank_p2p_overdue':        '',
    'sl_id_nbank_p2p_fraud':          '',
    'sl_id_nbank_p2p_lost':           '',
    'sl_id_nbank_p2p_refuse':         '',
    'sl_id_nbank_mc_bad':             '',
    'sl_id_nbank_mc_overdue':         '',
    'sl_id_nbank_mc_fraud':           '',
    'sl_id_nbank_mc_lost':            '',
    'sl_id_nbank_mc_refuse':          '',
    'sl_id_nbank_ca_bad':             '',
    'sl_id_nbank_ca_overdue':         '',
    'sl_id_nbank_ca_lost':            '',
    'sl_id_nbank_ca_refuse':          '',
    'sl_id_nbank_com_bad':            '',
    'sl_id_nbank_com_overdue':        '',
    'sl_id_nbank_com_lost':           '',
    'sl_id_nbank_com_refuse':         '',
    'sl_id_nbank_cf_bad':             '',
    'sl_id_nbank_cf_overdue':         '',
    'sl_id_nbank_cf_fraud':           '',
    'sl_id_nbank_cf_lost':            '',
    'sl_id_nbank_cf_refuse':          '',
    'sl_id_nbank_other_bad':          '',
    'sl_id_nbank_other_overdue':      '',
    'sl_id_nbank_other_fraud':        '',
    'sl_id_nbank_other_lost':         '',
    'sl_id_nbank_other_refuse':       '',
    'sl_lm_cell_abnormal':            '',
    'sl_lm_cell_bank_bad':            '',
    'sl_lm_cell_bank_overdue':        '',
    'sl_lm_cell_bank_fraud':          '',
    'sl_lm_cell_bank_lost':           '',
    'sl_lm_cell_bank_refuse':         '',
    'sl_lm_cell_phone_overdue':       '',
    'sl_lm_cell_nbank_p2p_bad':       '',
    'sl_lm_cell_nbank_p2p_overdue':   '',
    'sl_lm_cell_nbank_p2p_fraud':     '',
    'sl_lm_cell_nbank_p2p_lost':      '',
    'sl_lm_cell_nbank_p2p_refuse':    '',
    'sl_lm_cell_nbank_mc_bad':        '',
    'sl_lm_cell_nbank_mc_overdue':    '',
    'sl_lm_cell_nbank_mc_fraud':      '',
    'sl_lm_cell_nbank_mc_lost':       '',
    'sl_lm_cell_nbank_mc_refuse':     '',
    'sl_lm_cell_nbank_ca_bad':        '',
    'sl_lm_cell_nbank_ca_overdue':    '',
    'sl_lm_cell_nbank_ca_lost':       '',
    'sl_lm_cell_nbank_ca_refuse':     '',
    'sl_lm_cell_nbank_com_bad':       '',
    'sl_lm_cell_nbank_com_overdue':   '',
    'sl_lm_cell_nbank_com_lost':      '',
    'sl_lm_cell_nbank_com_refuse':    '',
    'sl_lm_cell_nbank_cf_bad':        '',
    'sl_lm_cell_nbank_cf_overdue':    '',
    'sl_lm_cell_nbank_cf_fraud':      '',
    'sl_lm_cell_nbank_cf_lost':       '',
    'sl_lm_cell_nbank_cf_refuse':     '',
    'sl_lm_cell_nbank_other_bad':     '',
    'sl_lm_cell_nbank_other_overdue': '',
    'sl_lm_cell_nbank_other_fraud':   '',
    'sl_lm_cell_nbank_other_lost':    '',
    'sl_lm_cell_nbank_other_refuse':  '',
    'sl_cell_abnormal':               '',
    'sl_cell_bank_bad':               '',
    'sl_cell_bank_overdue':           '',
    'sl_cell_bank_fraud':             '',
    'sl_cell_bank_lost':              '',
    'sl_cell_bank_refuse':            '',
    'sl_cell_p2p_bad':                '',
    'sl_cell_p2p_overdue':            '',
    'sl_cell_p2p_fraud':              '',
    'sl_cell_p2p_lost':               '',
    'sl_cell_p2p_refuse':             '',
    'sl_cell_phone_overdue':          '',
    'sl_cell_nbank_p2p_bad':          '',
    'sl_cell_nbank_p2p_overdue':      '',
    'sl_cell_nbank_p2p_fraud':        '',
    'sl_cell_nbank_p2p_lost':         '',
    'sl_cell_nbank_p2p_refuse':       '',
    'sl_cell_nbank_mc_bad':           '',
    'sl_cell_nbank_mc_overdue':       '',
    'sl_cell_nbank_mc_fraud':         '',
    'sl_cell_nbank_mc_lost':          '',
    'sl_cell_nbank_mc_refuse':        '',
    'sl_cell_nbank_ca_bad':           '',
    'sl_cell_nbank_ca_overdue':       '',
    'sl_cell_nbank_ca_lost':          '',
    'sl_cell_nbank_ca_refuse':        '',
    'sl_cell_nbank_com_bad':          '',
    'sl_cell_nbank_com_overdue':      '',
    'sl_cell_nabnk_com_lost':         '',
    'sl_cell_nbank_com_refuse':       '',
    'sl_cell_nbank_cf_bad':           '',
    'sl_cell_nbank_cf_overdue':       '',
    'sl_cell_nbank_cf_fraud':         '',
    'sl_cell_nabnk_cf_lost':          '',
    'sl_cell_nbank_cf_refuse':        '',
    'sl_cell_nbank_other_bad':        '',
    'sl_cell_nbank_other_overdue':    '',
    'sl_cell_nbank_other_fraud':      '',
    'sl_cell_nabnk_other_lost':       '',
    'sl_cell_nbank_other_refuse':     '',
    'sl_gid_bank_bad':                '',
    'sl_gid_bank_overdue':            '',
    'sl_gid_bank_fraud':              '',
    'sl_gid_bank_lost':               '',
    'sl_gid_bank_refuse':             '',
    'sl_gid_p2p_bad':                 '',
    'sl_gid_p2p_overdue':             '',
    'sl_gid_p2p_fraud':               '',
    'sl_gid_p2p_lost':                '',
    'sl_gid_p2p_refuse':              '',
    'sl_gid_phone_overdue':           '',
    'sl_gid_nbank_p2p_bad':           '',
    'sl_gid_nbank_p2p_overdue':       '',
    'sl_gid_nbank_p2p_fraud':         '',
    'sl_gid_nbank_p2p_lost':          '',
    'sl_gid_nbank_p2p_refuse':        '',
    'sl_gid_nbank_mc_bad':            '',
    'sl_gid_nbank_mc_overdue':        '',
    'sl_gid_nbank_mc_fraud':          '',
    'sl_gid_nbank_mc_lost':           '',
    'sl_gid_nbank_mc_refuse':         '',
    'sl_gid_nbank_ca_bad':            '',
    'sl_gid_nbank_ca_overdue':        '',
    'sl_gid_nbank_ca_lost':           '',
    'sl_gid_nbank_ca_refuse':         '',
    'sl_gid_nbank_com_bad':           '',
    'sl_gid_nbank_com_overdue':       '',
    'sl_gid_nbank_com_lost':          '',
    'sl_gid_nbank_com_refuse':        '',
    'sl_gid_nbank_cf_bad':            '',
    'sl_gid_nbank_cf_overdue':        '',
    'sl_gid_nbank_cf_fraud':          '',
    'sl_gid_nbank_cf_lost':           '',
    'sl_gid_nbank_cf_refuse':         '',
    'sl_gid_nbank_other_bad':         '',
    'sl_gid_nbank_other_overdue':     '',
    'sl_gid_nbank_other_fraud':       '',
    'sl_gid_nbank_other_lost':        '',
    'sl_gid_nbank_other_refuse':      ''

}
# 行为评估
flag_behavior = {
    # 航旅行为
    'at_month':                 '',
    'at_max_city':              '',
    'at_q0_total_num':          '',
    'at_q0_first_num':          '',
    'at_q0_business_num':       '',
    'at_q0_economy_num':        '',
    'at_q0_max_city':           '',
    'at_q1_total_num':          '',
    'at_q1_first_num':          '',
    'at_q1_business_num':       '',
    'at_q1_economy_num':        '',
    'at_q1_max_city':           '',
    'at_q2_total_num':          '',
    'at_q2_first_num':          '',
    'at_q2_business_num':       '',
    'at_q2_economy_num':        '',
    'at_q2_max_city':           '',
    'at_q3_total_num':          '',
    'at_q3_first_num':          '',
    'at_q3_business_num':       '',
    'at_q3_economy_num':        '',
    'at_q3_max_city':           '',
    'at_q4_total_num':          '',
    'at_q4_first_num':          '',
    'at_q4_business_num':       '',
    'at_q4_economy_num':        '',
    'at_q4_max_city':           '',
    # 媒体阅览
    'media_tot_m3_visitdays':   '',
    'media_tot_m12_visitdays':  '',
    'media_max_m3_days_prop':   '',
    'media_max_m12_days_prop':  '',
    'media_max_m3_days':        '',
    'media_max_m3_cate':        '',
    'media_max_m12_days':       '',
    'media_max_m12_cate':       '',
    'media_tot_m3_catenum':     '',
    'media_tot_m12_catenum':    '',
    'media_m3_CJ_visitdays':    '',
    'media_m3_WXYS_visitdays':  '',
    'media_m3_MYYE_visitdays':  '',
    'media_m12_CJ_visitdays':   '',
    'media_m12_WXYS_visitdays': '',
    'media_m12_MYYE_visitdays': '',
    # 社交信息
    'sr_match_type':            '',
    'sr_user_type':             '',
    'sr_gender':                '',
    'sr_reg_date':              '',
    'sr_birthday':              '',
    'sr_int_tag':               '',
    'sr_talent':                '',
    'sr_level':                 '',
    'sr_follow_num':            '',
    'sr_fans_num':              '',
    'sr_spread':                '',
    'sr_industry':              '',
    'sr_location':              '',
    'sr_weibo_num':             '',
    'sr_nick':                  '',
    'sr_blog':                  '',
    'sr_domain':                ''
}
# 消费评估
flag_consume = {
    # 月度收支
    'acm_card_index':           '',
    'acm_m1_debit_balance':     '',
    'acm_m1_debit_out':         '',
    'acm_m1_debit_invest':      '',
    'acm_m1_debit_repay':       '',
    'acm_m1_debit_in':          '',
    'acm_m1_credit_out':        '',
    'acm_m1_credit_cash':       '',
    'acm_m1_credit_in':         '',
    'acm_m1_credit_def':        '',
    'acm_m1_loan':              '',
    'acm_m2_debit_balance':     '',
    'acm_m2_debit_out':         '',
    'acm_m2_debit_invest':      '',
    'acm_m2_debit_repay':       '',
    'acm_m2_debit_in':          '',
    'acm_m2_credit_out':        '',
    'acm_m2_credit_cash':       '',
    'acm_m2_credit_in':         '',
    'acm_m2_credit_def':        '',
    'acm_m2_loan':              '',
    'acm_m3_debit_balance':     '',
    'acm_m3_debit_out':         '',
    'acm_m3_debit_invest':      '',
    'acm_m3_debit_repay':       '',
    'acm_m3_debit_in':          '',
    'acm_m3_credit_out':        '',
    'acm_m3_credit_cash':       '',
    'acm_m3_credit_in':         '',
    'acm_m3_credit_def':        '',
    'acm_m3_loan':              '',
    'acm_m4_debit_balance':     '',
    'acm_m4_debit_out':         '',
    'acm_m4_debit_invest':      '',
    'acm_m4_debit_repay':       '',
    'acm_m4_debit_in':          '',
    'acm_m4_credit_out':        '',
    'acm_m4_credit_cash':       '',
    'acm_m4_credit_in':         '',
    'acm_m4_credit_def':        '',
    'acm_m4_loan':              '',
    'acm_m5_debit_balance':     '',
    'acm_m5_debit_out':         '',
    'acm_m5_debit_invest':      '',
    'acm_m5_debit_repay':       '',
    'acm_m5_debit_in':          '',
    'acm_m5_credit_out':        '',
    'acm_m5_credit_cash':       '',
    'acm_m5_credit_in':         '',
    'acm_m5_credit_def':        '',
    'acm_m5_loan':              '',
    'acm_m6_debit_balance':     '',
    'acm_m6_debit_out':         '',
    'acm_m6_debit_invest':      '',
    'acm_m6_debit_repay':       '',
    'acm_m6_debit_in':          '',
    'acm_m6_credit_out':        '',
    'acm_m6_credit_cash':       '',
    'acm_m6_credit_in':         '',
    'acm_m6_credit_def':        '',
    'acm_m6_loan':              '',
    'acm_m7m9_debit_balance':   '',
    'acm_m7m9_debit_out':       '',
    'acm_m7m9_debit_invest':    '',
    'acm_m7m9_debit_repay':     '',
    'acm_m7m9_debit_in':        '',
    'acm_m7m9_credit_out':      '',
    'acm_m7m9_credit_cash':     '',
    'acm_m7m9_credit_in':       '',
    'acm_m7m9_credit_def':      '',
    'acm_m7m9_loan':            '',
    'acm_m10m12_debit_balance': '',
    'acm_m10m12_debit_out':     '',
    'acm_m10m12_debit_invest':  '',
    'acm_m10m12_debit_repay':   '',
    'acm_m10m12_debit_in':      '',
    'acm_m10m12_credit_out':    '',
    'acm_m10m12_credit_cash':   '',
    'acm_m10m12_credit_in':     '',
    'acm_m10m12_credit_def':    '',
    'acm_m10m12_loan':          '',
    'acm_m13m15_debit_balance': '',
    'acm_m13m15_debit_out':     '',
    'acm_m13m15_debit_invest':  '',
    'acm_m13m15_debit_repay':   '',
    'acm_m13m15_debit_in':      '',
    'acm_m13m15_credit_out':    '',
    'acm_m13m15_credit_cash':   '',
    'acm_m13m15_credit_in':     '',
    'acm_m13m15_credit_def':    '',
    'acm_m13m15_loan':          '',
    'acm_m16m18_debit_balance': '',
    'acm_m16m18_debit_out':     '',
    'acm_m16m18_debit_invest':  '',
    'acm_m16m18_debit_repay':   '',
    'acm_m16m18_debit_in':      '',
    'acm_m16m18_credit_out':    '',
    'acm_m16m18_credit_cash':   '',
    'acm_m16m18_credit_in':     '',
    'acm_m16m18_credit_def':    '',
    'acm_m16m18_loan':          '',
    # 商品消费
    'cons_cont':                '',
    'cons_time_recent':         '',
    'cons_tot_m3_num':          '',
    'cons_tot_m3_pay':          '',
    'cons_tot_m3_p_catenum':    '',
    'cons_tot_m3_v_catenum':    '',
    'cons_tot_m3_visits':       '',
    'cons_tot_m12_num':         '',
    'cons_tot_m12_pay':         '',
    'cons_tot_m12_p_catenum':   '',
    'cons_tot_m12_v_catenum':   '',
    'cons_tot_m12_visits':      '',
    'cons_max_m3_num':          '',
    'cons_max_m3_pay':          '',
    'cons_max_m3_paycate':      '',
    'cons_max_m12_num':         '',
    'cons_max_m12_pay':         '',
    'cons_max_m12_paycate':     '',
    'cons_m3_RYBH_num':         '',
    'cons_m3_RYBH_pay':         '',
    'cons_m3_JYDQ_num':         '',
    'cons_m3_JYDQ_pay':         '',
    'cons_m3_MYYP_num':         '',
    'cons_m3_MYYP_pay':         '',
    'cons_m12_RYBH_num':        '',
    'cons_m12_RYBH_pay':        '',
    'cons_m12_JYDQ_num':        '',
    'cons_m12_JYDQ_pay':        '',
    'cons_m12_MYYP_num':        '',
    'cons_m12_MYYP_pay':        '',
    # 银行消费支付
    'pc_thm1_pay':              '',
    'pc_thm1_num':              '',
    'pc_thm1_1st_pay_mcc':      '',
    'pc_thm1_1st_num_mcc':      '',
    'pc_thm1_2nd_pay_mcc':      '',
    'pc_thm1_2nd_num_mcc':      '',
    'pc_thm1_3rd_pay_mcc':      '',
    'pc_thm1_3rd_num_mcc':      '',
    'pc_thm1_max_num_pvn':      '',
    'pc_thm1_night_pay':        '',
    'pc_thm1_night_num':        '',
    'pc_thm2_pay':              '',
    'pc_thm2_num':              '',
    'pc_thm2_1st_pay_mcc':      '',
    'pc_thm2_1st_num_mcc':      '',
    'pc_thm2_2nd_pay_mcc':      '',
    'pc_thm2_2nd_num_mcc':      '',
    'pc_thm2_3rd_pay_mcc':      '',
    'pc_thm2_3rd_num_mcc':      '',
    'pc_thm2_max_num_pvn':      '',
    'pc_thm2_night_pay':        '',
    'pc_thm2_night_num':        '',
    'pc_thm3_pay':              '',
    'pc_thm3_num':              '',
    'pc_thm3_1st_pay_mcc':      '',
    'pc_thm3_1st_num_mcc':      '',
    'pc_thm3_2nd_pay_mcc':      '',
    'pc_thm3_2nd_num_mcc':      '',
    'pc_thm3_3rd_pay_mcc':      '',
    'pc_thm3_3rd_num_mcc':      '',
    'pc_thm3_max_num_pvn':      '',
    'pc_thm3_night_pay':        '',
    'pc_thm3_night_num':        '',
    'pc_thm4_pay':              '',
    'pc_thm4_num':              '',
    'pc_thm4_1st_pay_mcc':      '',
    'pc_thm4_1st_num_mcc':      '',
    'pc_thm4_2nd_pay_mcc':      '',
    'pc_thm4_2nd_num_mcc':      '',
    'pc_thm4_3rd_pay_mcc':      '',
    'pc_thm4_3rd_num_mcc':      '',
    'pc_thm4_max_num_pvn':      '',
    'pc_thm4_night_pay':        '',
    'pc_thm4_night_num':        '',
    'pc_thm5_pay':              '',
    'pc_thm5_num':              '',
    'pc_thm5_1st_pay_mcc':      '',
    'pc_thm5_1st_num_mcc':      '',
    'pc_thm5_2nd_pay_mcc':      '',
    'pc_thm5_2nd_num_mcc':      '',
    'pc_thm5_3rd_pay_mcc':      '',
    'pc_thm5_3rd_num_mcc':      '',
    'pc_thm5_max_num_pvn':      '',
    'pc_thm5_night_pay':        '',
    'pc_thm5_night_num':        '',
    'pc_thm6_pay':              '',
    'pc_thm6_num':              '',
    'pc_thm6_1st_pay_mcc':      '',
    'pc_thm6_1st_num_mcc':      '',
    'pc_thm6_2nd_pay_mcc':      '',
    'pc_thm6_2nd_num_mcc':      '',
    'pc_thm6_3rd_pay_mcc':      '',
    'pc_thm6_3rd_num_mcc':      '',
    'pc_thm6_max_num_pvn':      '',
    'pc_thm6_night_pay':        '',
    'pc_thm6_night_num':        '',
    'pc_thm7_pay':              '',
    'pc_thm7_num':              '',
    'pc_thm7_1st_pay_mcc':      '',
    'pc_thm7_1st_num_mcc':      '',
    'pc_thm7_2nd_pay_mcc':      '',
    'pc_thm7_2nd_num_mcc':      '',
    'pc_thm7_3rd_pay_mcc':      '',
    'pc_thm7_3rd_num_mcc':      '',
    'pc_thm7_max_num_pvn':      '',
    'pc_thm7_night_pay':        '',
    'pc_thm7_night_num':        '',
    'pc_thm8_pay':              '',
    'pc_thm8_num':              '',
    'pc_thm8_1st_pay_mcc':      '',
    'pc_thm8_1st_num_mcc':      '',
    'pc_thm8_2nd_pay_mcc':      '',
    'pc_thm8_2nd_num_mcc':      '',
    'pc_thm8_3rd_pay_mcc':      '',
    'pc_thm8_3rd_num_mcc':      '',
    'pc_thm8_max_num_pvn':      '',
    'pc_thm8_night_pay':        '',
    'pc_thm8_night_num':        '',
    'pc_thm9_pay':              '',
    'pc_thm9_num':              '',
    'pc_thm9_1st_pay_mcc':      '',
    'pc_thm9_1st_num_mcc':      '',
    'pc_thm9_2nd_pay_mcc':      '',
    'pc_thm9_2nd_num_mcc':      '',
    'pc_thm9_3rd_pay_mcc':      '',
    'pc_thm9_3rd_num_mcc':      '',
    'pc_thm9_max_num_pvn':      '',
    'pc_thm9_night_pay':        '',
    'pc_thm9_night_num':        '',
    'pc_thm10_pay':             '',
    'pc_thm10_num':             '',
    'pc_thm10_1st_pay_mcc':     '',
    'pc_thm10_1st_num_mcc':     '',
    'pc_thm10_2nd_pay_mcc':     '',
    'pc_thm10_2nd_num_mcc':     '',
    'pc_thm10_3rd_pay_mcc':     '',
    'pc_thm10_3rd_num_mcc':     '',
    'pc_thm10_max_num_pvn':     '',
    'pc_thm10_night_pay':       '',
    'pc_thm10_night_num':       '',
    'pc_thm11_pay':             '',
    'pc_thm11_num':             '',
    'pc_thm11_1st_pay_mcc':     '',
    'pc_thm11_1st_num_mcc':     '',
    'pc_thm11_2nd_pay_mcc':     '',
    'pc_thm11_2nd_num_mcc':     '',
    'pc_thm11_3rd_pay_mcc':     '',
    'pc_thm11_3rd_num_mcc':     '',
    'pc_thm11_max_num_pvn':     '',
    'pc_thm11_night_pay':       '',
    'pc_thm11_night_num':       '',
    'pc_thm12_pay':             '',
    'pc_thm12_num':             '',
    'pc_thm12_1st_pay_mcc':     '',
    'pc_thm12_1st_num_mcc':     '',
    'pc_thm12_2nd_pay_mcc':     '',
    'pc_thm12_2nd_num_mcc':     '',
    'pc_thm12_3rd_pay_mcc':     '',
    'pc_thm12_3rd_num_mcc':     '',
    'pc_thm12_max_num_pvn':     '',
    'pc_thm12_night_pay':       '',
    'pc_thm12_night_num':       '',
}  # 对外关系
flag_invest = {}
# 刑事记录
flag_law = {}