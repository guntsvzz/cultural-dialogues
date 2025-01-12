from langchain_core.pydantic_v1 import BaseModel, Field

# Define the data structure for Personal Medical Information.
class HofstedeDimension(BaseModel):
    pdi : str = Field(..., description="Power Distance Index (PDI): Examine the balance of authority and roles (e.g., leadership vs. community).", 
                      enum=["low", "medium", "high"])
    idv : str = Field(..., description="Individualism vs. Collectivism (IDV): Determine whether the dialogue emphasizes individual goals or collective well-being.", 
                      enum=["low", "medium", "high"])
    mas : str = Field(..., description="Masculinity vs. Femininity (MAS): Evaluate whether the focus is on competition and achievement or care, cooperation, and harmony.", 
                      enum=["low", "medium", "high"])
    uai : str = Field(..., description="Uncertainty Avoidance Index (UAI): Assess whether the dialogue reflects comfort with change and adaptability or a preference for tradition and stability.", 
                      enum=["low", "medium", "high"])
    lto : str = Field(..., description="Long-Term vs. Short-Term Orientation (LTO): Consider how traditions are preserved or balanced with short-term flexibility.", 
                      enum=["low", "medium", "high"])
    ivr : str = Field(..., description="Indulgence vs. Restraint (IVR): Identify expressions of celebration, emotional freedom, or restraint in behavior.", 
                      enum=["low", "medium", "high"])