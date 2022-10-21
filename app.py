from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime


class SubModel(BaseModel):
    field1: str
    field2: int


class Model(BaseModel):
    str_field: str
    lst_field: list[str]
    datetime_field: datetime
    subfield: list[SubModel]


app = FastAPI()

# EASY

@app.post("/sdr", response_model=Model)
def sdr(p: Model):
    j = p.json()
    r = Model.parse_raw(j)
    return r

@app.post("/_s_dr", response_model=Model)
def _s_dr(p: Model):
    return p


@app.post("/_s_d_r")
def _s_d_r(p: Model):
    return p


@app.post("/_sdr", response_model=Model)
def _sdr(p: Model):
    r = Model(str_field=p.str_field, lst_field=p.lst_field, datetime_field=p.datetime_field, subfield=p.subfield)
    return r

# NUM

@app.post("/sdr/{num}", response_model=Model)
def sdr_num(num: int, p: Model):
    for _ in range(num):
        j = p.json()
        r = Model.parse_raw(j)
    return r


@app.post("/_sdr/{num}", response_model=Model)
def _sdr_num(num: int, p: Model):
    for _ in range(num):
        r = Model(str_field=p.str_field, lst_field=p.lst_field, datetime_field=p.datetime_field, subfield=p.subfield)
    return r


# TRANSFORMATION

class ResponseModel(BaseModel):
    str_field: str
    lst_field: list[str]
    datetime_field: datetime
    subfield: list[SubModel]

    extra_field1: str
    extra_field2: SubModel


@app.post("/sdrt", response_model=ResponseModel)
def sdrt(p: Model):
    j = p.dict()
    j["extra_field1"] = "extra_field1"
    j["extra_field2"] = j["subfield"][0]
    r = ResponseModel.parse_obj(j)
    return r


@app.post("/s_drt", response_model=ResponseModel)
def s_drt(p: Model):
    j = p.dict()
    j["extra_field1"] = "extra_field1"
    j["extra_field2"] = j["subfield"][0]
    return j

@app.post("/_s_drt", response_model=ResponseModel)
def _s_drt(p: Model):
    r = ResponseModel(str_field=p.str_field, lst_field=p.lst_field, datetime_field=p.datetime_field,
                      subfield=p.subfield, extra_field1="extra_field1", extra_field2=p.subfield[0])
    return r

@app.post("/_s_d_rt")
def _s_d_rt(p: Model):
    r = ResponseModel(str_field=p.str_field, lst_field=p.lst_field, datetime_field=p.datetime_field,
                      subfield=p.subfield, extra_field1="extra_field1", extra_field2=p.subfield[0])
    return r
