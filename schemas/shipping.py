from pydantic import BaseModel, Json, ConfigDict

class ShippingCalculateSchema(BaseModel):
    """
    Define como informações devem ser fornecidas para fazer o cálculo de frete
    """

    #Erro configura o pydantic para aceitar conversão de número para string
    model_config = ConfigDict(coerce_numbers_to_str=True)

    from_postal_code: str = 24241265
    to_postal_code: str = 22451900
    package_height: int = 4
    package_width: int = 12
    package_length: int = 17
    package_weight: float = 0.3

class ShippingCalculateViewSchema(BaseModel):
    """
    Define como a informação é retornada
    """
    response: Json[dict]