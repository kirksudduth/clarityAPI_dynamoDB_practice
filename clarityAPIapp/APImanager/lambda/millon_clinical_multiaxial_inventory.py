import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('clarityAPI')


def lambda_handler(event, context):

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET millon_clinical_multiaxial_inventory_iv_pg1_a = :mcmiipg1a, millon_clinical_multiaxial_inventory_iv_pg1_b = :mcmiipg1b, millon_clinical_multiaxial_inventory_iv_pg1_c = :mcmiipg1c, millon_clinical_multiaxial_inventory_iv_pg1_d = :mcmiipg1d, millon_clinical_multiaxial_inventory_iv_pg1_e = :mcmiipg1e, millon_clinical_multiaxial_inventory_iv_pg1_f = :mcmiipg1f, millon_clinical_multiaxial_inventory_iv_pg1_g = :mcmiipg1g, millon_clinical_multiaxial_inventory_iv_pg1_h = :mcmiipg1h, millon_clinical_multiaxial_inventory_iv_pg1_i = :mcmiipg1i, millon_clinical_multiaxial_inventory_iv_pg1_j = :mcmiipg1j, millon_clinical_multiaxial_inventory_iv_pg1_k = :mcmiipg1k, millon_clinical_multiaxial_inventory_iv_pg1_l = :mcmiipg1l, millon_clinical_multiaxial_inventory_iv_pg1_m = :mcmiipg1m, millon_clinical_multiaxial_inventory_iv_pg1_n = :mcmiipg1n, millon_clinical_multiaxial_inventory_iv_pg1_o = :mcmiipg1o, millon_clinical_multiaxial_inventory_iv_pg1_p = :mcmiipg1p, millon_clinical_multiaxial_inventory_iv_pg1_q = :mcmiipg1q, millon_clinical_multiaxial_inventory_iv_pg1_r = :mcmiipg1r, millon_clinical_multiaxial_inventory_iv_pg1_s = :mcmiipg1s, millon_clinical_multiaxial_inventory_iv_pg1_t = :mcmiipg1t, millon_clinical_multiaxial_inventory_iv_pg1_u = :mcmiipg1u, millon_clinical_multiaxial_inventory_iv_pg1_v = :mcmiipg1v, millon_clinical_multiaxial_inventory_iv_pg1_w = :mcmiipg1w, millon_clinical_multiaxial_inventory_iv_pg1_x = :mcmiipg1x, millon_clinical_multiaxial_inventory_iv_pg1_y = :mcmiipg1y, millon_clinical_multiaxial_inventory_iv_pg1_z = :mcmiipg1z, millon_clinical_multiaxial_inventory_iv_pg1_aa = :mcmiipg1aa, millon_clinical_multiaxial_inventory_iv_pg1_bb = :mcmiipg1bb, millon_clinical_multiaxial_inventory_iv_pg1_cc = :mcmiipg1cc, millon_clinical_multiaxial_inventory_iv_pg1_dd = :mcmiipg1dd, millon_clinical_multiaxial_inventory_iv_pg1_ee = :mcmiipg1ee, millon_clinical_multiaxial_inventory_iv_pg1_ff = :mcmiipg1ff",
        ExpressionAttributeValues={
            ":mcmiipg1a": event['millon_clinical_multiaxial_inventory_iv_pg1_a'],
            ":mcmiipg1b": event['millon_clinical_multiaxial_inventory_iv_pg1_b'],
            ":mcmiipg1c": event['millon_clinical_multiaxial_inventory_iv_pg1_c'],
            ":mcmiipg1d": event['millon_clinical_multiaxial_inventory_iv_pg1_d'],
            ":mcmiipg1e": event['millon_clinical_multiaxial_inventory_iv_pg1_e'],
            ":mcmiipg1f": event['millon_clinical_multiaxial_inventory_iv_pg1_f'],
            ":mcmiipg1g": event['millon_clinical_multiaxial_inventory_iv_pg1_g'],
            ":mcmiipg1h": event['millon_clinical_multiaxial_inventory_iv_pg1_h'],
            ":mcmiipg1i": event['millon_clinical_multiaxial_inventory_iv_pg1_i'],
            ":mcmiipg1j": event['millon_clinical_multiaxial_inventory_iv_pg1_j'],
            ":mcmiipg1k": event['millon_clinical_multiaxial_inventory_iv_pg1_k'],
            ":mcmiipg1l": event['millon_clinical_multiaxial_inventory_iv_pg1_l'],
            ":mcmiipg1m": event['millon_clinical_multiaxial_inventory_iv_pg1_m'],
            ":mcmiipg1n": event['millon_clinical_multiaxial_inventory_iv_pg1_n'],
            ":mcmiipg1o": event['millon_clinical_multiaxial_inventory_iv_pg1_o'],
            ":mcmiipg1p": event['millon_clinical_multiaxial_inventory_iv_pg1_p'],
            ":mcmiipg1q": event['millon_clinical_multiaxial_inventory_iv_pg1_q'],
            ":mcmiipg1r": event['millon_clinical_multiaxial_inventory_iv_pg1_r'],
            ":mcmiipg1s": event['millon_clinical_multiaxial_inventory_iv_pg1_s'],
            ":mcmiipg1t": event['millon_clinical_multiaxial_inventory_iv_pg1_t'],
            ":mcmiipg1u": event['millon_clinical_multiaxial_inventory_iv_pg1_u'],
            ":mcmiipg1v": event['millon_clinical_multiaxial_inventory_iv_pg1_v'],
            ":mcmiipg1w": event['millon_clinical_multiaxial_inventory_iv_pg1_w'],
            ":mcmiipg1x": event['millon_clinical_multiaxial_inventory_iv_pg1_x'],
            ":mcmiipg1y": event['millon_clinical_multiaxial_inventory_iv_pg1_y'],
            ":mcmiipg1z": event['millon_clinical_multiaxial_inventory_iv_pg1_z'],
            ":mcmiipg1aa": event['millon_clinical_multiaxial_inventory_iv_pg1_aa'],
            ":mcmiipg1bb": event['millon_clinical_multiaxial_inventory_iv_pg1_bb'],
            ":mcmiipg1cc": event['millon_clinical_multiaxial_inventory_iv_pg1_cc'],
            ":mcmiipg1dd": event['millon_clinical_multiaxial_inventory_iv_pg1_dd'],
            ":mcmiipg1ee": event['millon_clinical_multiaxial_inventory_iv_pg1_ee'],
            ":mcmiipg1ff": event['millon_clinical_multiaxial_inventory_iv_pg1_ff']
        },
        ReturnValues="UPDATED_NEW")

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET millon_clinical_multiaxial_inventory_iv_pg1_Raw_a = :mcmiipg1Ra, millon_clinical_multiaxial_inventory_iv_pg1_Raw_b = :mcmiipg1Rb, millon_clinical_multiaxial_inventory_iv_pg1_Raw_c = :mcmiipg1Rc, millon_clinical_multiaxial_inventory_iv_pg1_Raw_d = :mcmiipg1Rd, millon_clinical_multiaxial_inventory_iv_pg1_Raw_e = :mcmiipg1Re, millon_clinical_multiaxial_inventory_iv_pg1_Raw_f = :mcmiipg1Rf, millon_clinical_multiaxial_inventory_iv_pg1_Raw_g = :mcmiipg1Rg, millon_clinical_multiaxial_inventory_iv_pg1_Raw_h = :mcmiipg1Rh, millon_clinical_multiaxial_inventory_iv_pg1_Raw_i = :mcmiipg1Ri, millon_clinical_multiaxial_inventory_iv_pg1_Raw_j = :mcmiipg1Rj, millon_clinical_multiaxial_inventory_iv_pg1_Raw_k = :mcmiipg1Rk, millon_clinical_multiaxial_inventory_iv_pg1_Raw_l = :mcmiipg1Rl, millon_clinical_multiaxial_inventory_iv_pg1_Raw_m = :mcmiipg1Rm, millon_clinical_multiaxial_inventory_iv_pg1_Raw_n = :mcmiipg1Rn, millon_clinical_multiaxial_inventory_iv_pg1_Raw_o = :mcmiipg1Ro, millon_clinical_multiaxial_inventory_iv_pg1_Raw_p = :mcmiipg1Rp, millon_clinical_multiaxial_inventory_iv_pg1_Raw_q = :mcmiipg1Rq, millon_clinical_multiaxial_inventory_iv_pg1_Raw_r = :mcmiipg1Rr, millon_clinical_multiaxial_inventory_iv_pg1_Raw_s = :mcmiipg1Rs, millon_clinical_multiaxial_inventory_iv_pg1_Raw_t = :mcmiipg1Rt, millon_clinical_multiaxial_inventory_iv_pg1_Raw_u = :mcmiipg1Ru, millon_clinical_multiaxial_inventory_iv_pg1_Raw_v = :mcmiipg1Rv, millon_clinical_multiaxial_inventory_iv_pg1_Raw_w = :mcmiipg1Rw, millon_clinical_multiaxial_inventory_iv_pg1_Raw_x = :mcmiipg1Rx, millon_clinical_multiaxial_inventory_iv_pg1_Raw_y = :mcmiipg1Ry, millon_clinical_multiaxial_inventory_iv_pg1_Raw_z = :mcmiipg1Rz, millon_clinical_multiaxial_inventory_iv_pg1_Raw_aa = :mcmiipg1Raa, millon_clinical_multiaxial_inventory_iv_pg1_Raw_bb = :mcmiipg1Rbb, millon_clinical_multiaxial_inventory_iv_pg1_Raw_cc = :mcmiipg1Rcc, millon_clinical_multiaxial_inventory_iv_pg1_Raw_dd = :mcmiipg1Rdd, millon_clinical_multiaxial_inventory_iv_pg1_Raw_ee = :mcmiipg1Ree, millon_clinical_multiaxial_inventory_iv_pg1_Raw_ff = :mcmiipg1Rff",
        ExpressionAttributeValues={
            ":mcmiipg1Ra": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_a'],
            ":mcmiipg1Rb": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_b'],
            ":mcmiipg1Rc": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_c'],
            ":mcmiipg1Rd": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_d'],
            ":mcmiipg1Re": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_e'],
            ":mcmiipg1Rf": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_f'],
            ":mcmiipg1Rg": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_g'],
            ":mcmiipg1Rh": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_h'],
            ":mcmiipg1Ri": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_i'],
            ":mcmiipg1Rj": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_j'],
            ":mcmiipg1Rk": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_k'],
            ":mcmiipg1Rl": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_l'],
            ":mcmiipg1Rm": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_m'],
            ":mcmiipg1Rn": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_n'],
            ":mcmiipg1Ro": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_o'],
            ":mcmiipg1Rp": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_p'],
            ":mcmiipg1Rq": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_q'],
            ":mcmiipg1Rr": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_r'],
            ":mcmiipg1Rs": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_s'],
            ":mcmiipg1Rt": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_t'],
            ":mcmiipg1Ru": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_u'],
            ":mcmiipg1Rv": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_v'],
            ":mcmiipg1Rw": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_w'],
            ":mcmiipg1Rx": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_x'],
            ":mcmiipg1Ry": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_y'],
            ":mcmiipg1Rz": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_z'],
            ":mcmiipg1Raa": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_aa'],
            ":mcmiipg1Rbb": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_bb'],
            ":mcmiipg1Rcc": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_cc'],
            ":mcmiipg1Rdd": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_dd'],
            ":mcmiipg1Ree": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_ee'],
            ":mcmiipg1Rff": event['millon_clinical_multiaxial_inventory_iv_pg1_Raw_ff']
        },
        ReturnValues="UPDATED_NEW")

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET millon_clinical_multiaxial_inventory_iv_pg1_PR_a = :mcmiipg1PRa, millon_clinical_multiaxial_inventory_iv_pg1_PR_b = :mcmiipg1PRb, millon_clinical_multiaxial_inventory_iv_pg1_PR_c = :mcmiipg1PRc, millon_clinical_multiaxial_inventory_iv_pg1_PR_d = :mcmiipg1PRd, millon_clinical_multiaxial_inventory_iv_pg1_PR_e = :mcmiipg1PRe, millon_clinical_multiaxial_inventory_iv_pg1_PR_f = :mcmiipg1PRf, millon_clinical_multiaxial_inventory_iv_pg1_PR_g = :mcmiipg1PRg, millon_clinical_multiaxial_inventory_iv_pg1_PR_h = :mcmiipg1PRh, millon_clinical_multiaxial_inventory_iv_pg1_PR_i = :mcmiipg1PRi, millon_clinical_multiaxial_inventory_iv_pg1_PR_j = :mcmiipg1PRj, millon_clinical_multiaxial_inventory_iv_pg1_PR_k = :mcmiipg1PRk, millon_clinical_multiaxial_inventory_iv_pg1_PR_l = :mcmiipg1PRl, millon_clinical_multiaxial_inventory_iv_pg1_PR_m = :mcmiipg1PRm, millon_clinical_multiaxial_inventory_iv_pg1_PR_n = :mcmiipg1PRn, millon_clinical_multiaxial_inventory_iv_pg1_PR_o = :mcmiipg1PRo, millon_clinical_multiaxial_inventory_iv_pg1_PR_p = :mcmiipg1PRp, millon_clinical_multiaxial_inventory_iv_pg1_PR_q = :mcmiipg1PRq, millon_clinical_multiaxial_inventory_iv_pg1_PR_r = :mcmiipg1PRr, millon_clinical_multiaxial_inventory_iv_pg1_PR_s = :mcmiipg1PRs, millon_clinical_multiaxial_inventory_iv_pg1_PR_t = :mcmiipg1PRt, millon_clinical_multiaxial_inventory_iv_pg1_PR_u = :mcmiipg1PRu, millon_clinical_multiaxial_inventory_iv_pg1_PR_v = :mcmiipg1PRv, millon_clinical_multiaxial_inventory_iv_pg1_PR_w = :mcmiipg1PRw, millon_clinical_multiaxial_inventory_iv_pg1_PR_x = :mcmiipg1PRx, millon_clinical_multiaxial_inventory_iv_pg1_PR_y = :mcmiipg1PRy, millon_clinical_multiaxial_inventory_iv_pg1_PR_z = :mcmiipg1PRz, millon_clinical_multiaxial_inventory_iv_pg1_PR_aa = :mcmiipg1PRaa, millon_clinical_multiaxial_inventory_iv_pg1_PR_bb = :mcmiipg1PRbb, millon_clinical_multiaxial_inventory_iv_pg1_PR_cc = :mcmiipg1PRcc, millon_clinical_multiaxial_inventory_iv_pg1_PR_dd = :mcmiipg1PRdd, millon_clinical_multiaxial_inventory_iv_pg1_PR_ee = :mcmiipg1PRee, millon_clinical_multiaxial_inventory_iv_pg1_PR_ff = :mcmiipg1PRff",
        ExpressionAttributeValues={
            ":mcmiipg1PRa": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_a'],
            ":mcmiipg1PRb": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_b'],
            ":mcmiipg1PRc": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_c'],
            ":mcmiipg1PRd": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_d'],
            ":mcmiipg1PRe": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_e'],
            ":mcmiipg1PRf": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_f'],
            ":mcmiipg1PRg": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_g'],
            ":mcmiipg1PRh": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_h'],
            ":mcmiipg1PRi": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_i'],
            ":mcmiipg1PRj": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_j'],
            ":mcmiipg1PRk": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_k'],
            ":mcmiipg1PRl": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_l'],
            ":mcmiipg1PRm": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_m'],
            ":mcmiipg1PRn": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_n'],
            ":mcmiipg1PRo": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_o'],
            ":mcmiipg1PRp": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_p'],
            ":mcmiipg1PRq": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_q'],
            ":mcmiipg1PRr": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_r'],
            ":mcmiipg1PRs": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_s'],
            ":mcmiipg1PRt": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_t'],
            ":mcmiipg1PRu": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_u'],
            ":mcmiipg1PRv": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_v'],
            ":mcmiipg1PRw": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_w'],
            ":mcmiipg1PRx": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_x'],
            ":mcmiipg1PRy": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_y'],
            ":mcmiipg1PRz": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_z'],
            ":mcmiipg1PRaa": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_aa'],
            ":mcmiipg1PRbb": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_bb'],
            ":mcmiipg1PRcc": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_cc'],
            ":mcmiipg1PRdd": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_dd'],
            ":mcmiipg1PRee": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_ee'],
            ":mcmiipg1PRff": event['millon_clinical_multiaxial_inventory_iv_pg1_PR_ff']
        },
        ReturnValues="UPDATED_NEW")

    table.update_item(
        Key={
            'PK': event['PK'],
            'SK': event['SK']
        },
        UpdateExpression="SET millon_clinical_multiaxial_inventory_iv_pg1_BR_a = :mcmiipg1BRa, millon_clinical_multiaxial_inventory_iv_pg1_BR_b = :mcmiipg1BRb, millon_clinical_multiaxial_inventory_iv_pg1_BR_c = :mcmiipg1BRc, millon_clinical_multiaxial_inventory_iv_pg1_BR_d = :mcmiipg1BRd, millon_clinical_multiaxial_inventory_iv_pg1_BR_e = :mcmiipg1BRe, millon_clinical_multiaxial_inventory_iv_pg1_BR_f = :mcmiipg1BRf, millon_clinical_multiaxial_inventory_iv_pg1_BR_g = :mcmiipg1BRg, millon_clinical_multiaxial_inventory_iv_pg1_BR_h = :mcmiipg1BRh, millon_clinical_multiaxial_inventory_iv_pg1_BR_i = :mcmiipg1BRi, millon_clinical_multiaxial_inventory_iv_pg1_BR_j = :mcmiipg1BRj, millon_clinical_multiaxial_inventory_iv_pg1_BR_k = :mcmiipg1BRk, millon_clinical_multiaxial_inventory_iv_pg1_BR_l = :mcmiipg1BRl, millon_clinical_multiaxial_inventory_iv_pg1_BR_m = :mcmiipg1BRm, millon_clinical_multiaxial_inventory_iv_pg1_BR_n = :mcmiipg1BRn, millon_clinical_multiaxial_inventory_iv_pg1_BR_o = :mcmiipg1BRo, millon_clinical_multiaxial_inventory_iv_pg1_BR_p = :mcmiipg1BRp, millon_clinical_multiaxial_inventory_iv_pg1_BR_q = :mcmiipg1BRq, millon_clinical_multiaxial_inventory_iv_pg1_BR_r = :mcmiipg1BRr, millon_clinical_multiaxial_inventory_iv_pg1_BR_s = :mcmiipg1BRs, millon_clinical_multiaxial_inventory_iv_pg1_BR_t = :mcmiipg1BRt, millon_clinical_multiaxial_inventory_iv_pg1_BR_u = :mcmiipg1BRu, millon_clinical_multiaxial_inventory_iv_pg1_BR_v = :mcmiipg1BRv, millon_clinical_multiaxial_inventory_iv_pg1_BR_w = :mcmiipg1BRw, millon_clinical_multiaxial_inventory_iv_pg1_BR_x = :mcmiipg1BRx, millon_clinical_multiaxial_inventory_iv_pg1_BR_y = :mcmiipg1BRy, millon_clinical_multiaxial_inventory_iv_pg1_BR_z = :mcmiipg1BRz, millon_clinical_multiaxial_inventory_iv_pg1_BR_aa = :mcmiipg1BRaa, millon_clinical_multiaxial_inventory_iv_pg1_BR_bb = :mcmiipg1BRbb, millon_clinical_multiaxial_inventory_iv_pg1_BR_cc = :mcmiipg1BRcc, millon_clinical_multiaxial_inventory_iv_pg1_BR_dd = :mcmiipg1BRdd, millon_clinical_multiaxial_inventory_iv_pg1_BR_ee = :mcmiipg1BRee, millon_clinical_multiaxial_inventory_iv_pg1_BR_ff = :mcmiipg1BRff",
        ExpressionAttributeValues={
            ":mcmiipg1BRa": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_a'],
            ":mcmiipg1BRb": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_b'],
            ":mcmiipg1BRc": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_c'],
            ":mcmiipg1BRd": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_d'],
            ":mcmiipg1BRe": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_e'],
            ":mcmiipg1BRf": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_f'],
            ":mcmiipg1BRg": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_g'],
            ":mcmiipg1BRh": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_h'],
            ":mcmiipg1BRi": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_i'],
            ":mcmiipg1BRj": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_j'],
            ":mcmiipg1BRk": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_k'],
            ":mcmiipg1BRl": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_l'],
            ":mcmiipg1BRm": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_m'],
            ":mcmiipg1BRn": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_n'],
            ":mcmiipg1BRo": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_o'],
            ":mcmiipg1BRp": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_p'],
            ":mcmiipg1BRq": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_q'],
            ":mcmiipg1BRr": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_r'],
            ":mcmiipg1BRs": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_s'],
            ":mcmiipg1BRt": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_t'],
            ":mcmiipg1BRu": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_u'],
            ":mcmiipg1BRv": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_v'],
            ":mcmiipg1BRw": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_w'],
            ":mcmiipg1BRx": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_x'],
            ":mcmiipg1BRy": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_y'],
            ":mcmiipg1BRz": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_z'],
            ":mcmiipg1BRaa": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_aa'],
            ":mcmiipg1BRbb": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_bb'],
            ":mcmiipg1BRcc": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_cc'],
            ":mcmiipg1BRdd": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_dd'],
            ":mcmiipg1BRee": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_ee'],
            ":mcmiipg1BRff": event['millon_clinical_multiaxial_inventory_iv_pg1_BR_ff']
        },
        ReturnValues="UPDATED_NEW")
    return {
        'statusCode': 200,
        'message': json.dumps("If you are reading this... it worked!!")
    }
