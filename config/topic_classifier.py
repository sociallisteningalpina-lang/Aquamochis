#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clasificador de Temas para Comentarios de Campañas
Personalizable por campaña/producto
"""
import re
from typing import Callable

def create_topic_classifier() -> Callable[[str], str]:
    """
    Clasificador personalizado para la campaña Aquamochis de Alpina.
    """
    
    def classify_topic(comment: str) -> str:
        comment_lower = str(comment).lower()
        
        # CATEGORÍA 1: Coleccionismo y Juguetes (El núcleo de la campaña)
        if re.search(
            r'mochi|aqua|colecci|tengo|todos|falta|foca|mantarraya|'
            r'muñequito|juguete|animal|marino|obsesion|pece|feca|pulpo', 
            comment_lower
        ):
            return 'Coleccionismo y Juguetes'
        
        # CATEGORÍA 2: Críticas de Salud e Ingredientes (Lactosuero/Azúcar)
        if re.search(
            r'lactosuero|suero|az[úu]car|veneno|aditivo|ops|sello|'
            r'salud|ingrediente|nutrici|enfermedad|diabetes|grasa', 
            comment_lower
        ):
            return 'Salud e Ingredientes'
        
        # CATEGORÍA 3: Distribución y Disponibilidad (Oxxo, repetidos, falta de stock)
        if re.search(
            r'oxxo|ara|tienda|comprar|conseguir|donde|no hay|repetido|'
            r'lote|distribuci|no lleg[oó]|cartagena|turbaco|vender', 
            comment_lower
        ):
            return 'Distribución y Disponibilidad'
        
        # CATEGORÍA 4: Nostalgia y Sugerencias (Pedidos de juguetes antiguos)
        if re.search(
            r'antes|antiguo|vuelvan|ninjas|guerreros|ogros|2015|'
            r'fushiball|pega pega|tradici|recuerdo|infancia', 
            comment_lower
        ):
            return 'Nostalgia y Sugerencias'
        
        # CATEGORÍA 5: Precio y Valor (Quejas por el costo)
        if re.search(
            r'caro|precio|valor|costo|4\.?500|exageraci|ruina|plata', 
            comment_lower
        ):
            return 'Precio y Valor'
        
        # CATEGORÍA 6: Situación Institucional y Social (Contexto planta/salario)
        if re.search(
            r'planta|esclavista|instalaci|salario|m[ií]nimo|digna|'
            r'calles|protesta|explotando', 
            comment_lower
        ):
            return 'Situación Institucional y Social'
        
        # CATEGORÍA 7: Sentimiento Positivo / Feedback General
        if re.search(
            r'amo|lindo|hermoso|arte|bendici|gracias|excelente|mejor', 
            comment_lower
        ):
            return 'Sentimiento Positivo'
        
        # CATEGORÍA 8: Fuera de Tema / No Relevante
        if re.search(
            r'am[eé]n|jajaja|sticker|[0-9]{4}|ex[ -]novio|elon musk', 
            comment_lower
        ) or len(comment_lower.split()) < 2:
            return 'Fuera de Tema / Otros'
        
        return 'Otros'
    
    return classify_topic

# Ejemplo de uso:
classifier = create_topic_classifier()
print(classifier("Yogo Yogo no es yogur es lactosuero")) # Retorna: Salud e Ingredientes
print(classifier("me salieron 3 repetidos en el oxxo")) # Retorna: Distribución y Disponibilidad

# ============================================================================
# METADATA DE LA CAMPAÑA (OPCIONAL)
# ============================================================================

CAMPAIGN_METADATA = {
    'campaign_name': 'Alpina - Kéfir',
    'product': 'Kéfir Alpina',
    'categories': [
        'Preguntas sobre el Producto',
        'Comparación con Kéfir Casero/Artesanal',
        'Ingredientes y Salud',
        'Competencia y Disponibilidad',
        'Opinión General del Producto',
        'Fuera de Tema / No Relevante',
        'Otros'
    ],
    'version': '1.0',
    'last_updated': '2025-11-20'
}


def get_campaign_metadata() -> dict:
    """Retorna metadata de la campaña"""
    return CAMPAIGN_METADATA.copy()
