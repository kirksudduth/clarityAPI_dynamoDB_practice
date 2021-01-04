from pprint import pprint
import boto3

dynamodb = boto3.resource(
    'dynamodb')

table = dynamodb.Table('clarityAPI')

# pg6


def update_patient_parents(request, pk, sk):

    response = table.update_item(
        Key={
            'PK': pk,
            'SK': sk
        },
        AttributeUpdates={
            'father_first_name': {
                'Value': {form_value.father_first_name},
                'Action': 'ADD'
            },
            'father_last_name': {
                'Value': {form_value.father_last_name},
                'Action': 'ADD'
            },
            'mother_first_name': {
                'Value': {form_value.mother_first_name},
                'Action': 'ADD'
            },
            'mother_last_name': {
                'Value': {form_value.mother_last_name},
                'Action': 'ADD'
            },
            'guardian_first_name': {
                'Value': {form_value.guardian_first_name},
                'Action': 'ADD'
            },
            'guardian_last_name': {
                'Value': {form_value.guardian_last_name},
                'Action': 'ADD'
            },
            'guardian_gender': {
                'Value': {form_value.guardian_gender},
                'Action': 'ADD'
            }
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


# pg7
def update_patient_siblings(request, pk, sk):
    response = table.update_item(
        Key={
            'PK': pk,
            'SK': sk
        },
        AttributeUpdates={
            'is_only_child': {
                'Value': {boolean},
                'Action': 'ADD'
            },
            # research inserting lists into dynamodb
            # how from form to get multiple values into
            # empty list in dynamodb
            'siblings': {
                'Value': [
                    {
                        'sibling_first_name': {
                            'Value': {form_value.sibling_first_name},
                            'Action': 'ADD'
                        },
                        'sibling_last_name': {
                            'Value': {form_value.sibling_last_name},
                            'Action': 'ADD'
                        },
                        'sibling_gender': {
                            'Value': {form_value.sibling_gender},
                            'Action': 'ADD'
                        },
                        'sibling_dob': {
                            'Value': {form_value.sibling_dob},
                            'Action': 'ADD'
                        }
                    }
                ],
                'Action': 'ADD'
            },
        }
    )
    return response
# pg8


def update_patient_children(request, pk, sk):
    response = table.update_item(
        Key={
            'PK': pk,
            'SK': sk
        },
        AttributeUpdates={
            'has_children': {
                'Value': {boolean},
                'Action': 'ADD'
            },
            'children': {
                'Value': [
                    {
                        'child1_first_name': {
                            'Value': {form_value.child_first_name},
                            'Action': 'ADD'
                        },
                        'child1_last_name': {
                            'Value': {form_value.child_last_name},
                            'Action': 'ADD'
                        },
                        'child1_gender': {
                            'Value': {form_value.child_gender},
                            'Action': 'ADD'
                        },
                        'child1_dob': {
                            'Value': {form_value.child_dob},
                            'Action': 'ADD'
                        }
                    },
                    {
                        'child2_first_name': {
                            'Value': {form_value.child_first_name},
                            'Action': 'ADD'
                        },
                        'child2_last_name': {
                            'Value': {form_value.child_last_name},
                            'Action': 'ADD'
                        },
                        'child2_gender': {
                            'Value': {form_value.child_gender},
                            'Action': 'ADD'
                        },
                        'child2_dob': {
                            'Value': {form_value.child_dob},
                            'Action': 'ADD'
                        }
                    }
                ],
                'Action': 'ADD'
            },
        }
    )
    return response

# pg 9


def update_patient_marital_status(request, pk, sk):
    response = table.update_item(
        Key={
            'PK': pk,
            'SK': sk
        },
        AttributeUpdates={
            'marital_status': {
                'Value': {form_value.marital_status},
                'Action': 'ADD'
            },
            'spouse_first_name': {
                'Value': {form_value.spouse_first_name},
                'Action': 'ADD'
            },
            'spouse_last_name': {
                'Value': {form_value.spouse_last_name},
                'Action': 'ADD'
            },
            'spouse_gender': {
                'Value': {form_value.spouse_gender},
                'Action': 'ADD'
            },
            'spouse_dob': {
                'Value': {form_value.spouse_dob},
                'Action': 'ADD'
            }
        }
    )
    return response

# pg10


def patient_update_consent(request, pk, sk):
    response = table.update_item(
        Key={
            'PK': pk,
            'SK': sk
        },
        AttributeUpdates={
            'patient_consent': {
                'Value': {boolean},
                'Action': 'ADD'
            }
        }
    )
    return response


# pg13
def patient_update_interview_pg1(request, pk, sk):
    response = table.update_item(
        Key={
            'PK': pk,
            'SK': sk
        },
        AttributeUpdates={
            'interview_pg1_a': {
                'Value': {form_value.interview_pg1_a},
                'Action': 'ADD'
            },
            'interview_pg1_b': {
                'Value': {form_value.interview_pg1_b},
                'Action': 'ADD'
            }
        }
    )
    return response

# pg16


def patient_update_interview_pg2(request, pk, sk):
    response = table.update_item(
        Key={
            'PK': pk,
            'SK': sk
        },
        AttributeUpdates={
            'interview_pg2_a': {
                'Value': {form_value.interview_pg2_a},
                'Action': 'ADD'
            },
            'interview_pg2_b': {
                'Value': {form_value.interview_pg2_b},
                'Action': 'ADD'
            }
        }
    )
    return response


# pg17
def patient_update_interview_pg3(request, pk, sk):
    response = table.update_item(
        Key={
            'PK': pk,
            'SK': sk
        },
        AttributeUpdates={
            'interview_pg3_a': {
                'Value': {form_value.interview_pg3_a},
                'Action': 'ADD'
            },
            'interview_pg3_b': {
                'Value': {form_value.interview_pg3_b},
                'Action': 'ADD'
            }
        }
    )
    return response


def patient_update_interview_pg4(request, pk, sk):
    response = table.update_item(
        Key={
            'PK': pk,
            'SK': sk
        },
        AttributeUpdates={
            'interview_pg4_a': {
                'Value': {form_value.interview_pg4_a},
                'Action': 'ADD'
            },
            'interview_pg4_b': {
                'Value': {form_value.interview_pg4_b},
                'Action': 'ADD'
            }
        }
    )
    return response


def patient_update_interview_pg5(request, pk, sk):
    response = table.update_item(
        Key={
            'PK': pk,
            'SK': sk
        },
        AttributeUpdates={
            'interview_pg5_a': {
                'Value': {form_value.interview_pg5_a},
                'Action': 'ADD'
            },
            'interview_pg5_b': {
                'Value': {form_value.interview_pg5_b},
                'Action': 'ADD'
            },
            'interview_pg5_c': {
                'Value': {form_value.interview_pg5_c},
                'Action': 'ADD'
            },
            'interview_pg5_d': {
                'Value': {form_value.interview_pg5_d},
                'Action': 'ADD'
            }
        }
    )
    return response


def patient_update_interview_pg6(request, pk, sk):
    response = table.update_item(
        Key={
            'PK': pk,
            'SK': sk
        },
        AttributeUpdates={
            'interview_pg6_a': {
                'Value': {form_value.interview_pg6_a},
                'Action': 'ADD'
            },
            'interview_pg6_b': {
                'Value': {form_value.interview_pg6_b},
                'Action': 'ADD'
            }
        }
    )
    return response


def patient_update_interview_pg7(request, pk, sk):
    response = table.update_item(
        Key={
            'PK': pk,
            'SK': sk
        },
        AttributeUpdates={
            'interview_pg7_a': {
                'Value': {form_value.interview_pg7_a},
                'Action': 'ADD'
            },
            'interview_pg7_b': {
                'Value': {form_value.interview_pg7_b},
                'Action': 'ADD'
            }
        }
    )
    return response


def patient_update_interview_pg8(request, pk, sk):
    response = table.update_item(
        Key={
            'PK': pk,
            'SK': sk
        },
        AttributeUpdates={
            'interview_pg8_a': {
                'Value': {form_value.interview_pg8_a},
                'Action': 'ADD'
            }
        }
    )
    return response


def patient_update_interview_pg9(request, pk, sk):
    response = table.update_item(
        Key={
            'PK': pk,
            'SK': sk
        },
        AttributeUpdates={
            'interview_pg9_a': {
                'Value': {form_value.interview_pg9_a},
                'Action': 'ADD'
            },
            'interview_pg9_b': {
                'Value': {form_value.interview_pg9_b},
                'Action': 'ADD'
            },
            'interview_pg9_c': {
                'Value': {form_value.interview_pg9_c},
                'Action': 'ADD'
            }
        }
    )
    return response


def patient_update_family_pg1(request, pk, sk):
    response = table.update_item(
        Key={
            'PK': pk,
            'SK': sk
        },
        AttributeUpdates={
            'family_pg1_a': {
                'Value': {form_value.family_pg1_a},
                'Action': 'ADD'
            },
            'family_pg1_b': {
                'Value': {form_value.family_pg1_b},
                'Action': 'ADD'
            },
            'family_pg1_c': {
                'Value': {form_value.family_pg1_c},
                'Action': 'ADD'
            },
            'family_pg1_d': {
                'Value': {form_value.family_pg1_d},
                'Action': 'ADD'
            },
            'family_pg1_e': {
                'Value': {form_value.family_pg1_e},
                'Action': 'ADD'
            },
        }
    )
    return response


def patient_update_family_pg2(request, pk, sk):
    response = table.update_item(
        Key={
            'PK': pk,
            'SK': sk
        },
        AttributeUpdates={
            'family_pg2_a': {
                'Value': {form_value.family_pg2_a},
                'Action': 'ADD'
            },
            'family_pg2_b': {
                'Value': {form_value.family_pg2_b},
                'Action': 'ADD'
            },
            'family_pg2_c': {
                'Value': {form_value.family_pg2_c},
                'Action': 'ADD'
            }
        }
    )
